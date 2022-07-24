from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional

import dbt.exceptions
import mysql.connector
from dbt.adapters.base import Credentials
from dbt.adapters.sql import SQLConnectionManager
from dbt.events import AdapterLogger

logger = AdapterLogger("databend")


@dataclass
class DatabendCredentials(Credentials):
    """
    Databend connection credentials data class.
    """

    # pylint: disable=too-many-instance-attributes
    host: str = "localhost"
    port: Optional[int] = None
    database: Optional[str] = None
    schema: Optional[str] = "default"
    user: Optional[str] = "default"
    password: str = ""

    @property
    def type(self):
        return "databend"

    @property
    def unique_field(self):
        return self.host

    def __post_init__(self):
        if self.database is not None and self.database != self.schema:
            raise dbt.exceptions.RuntimeException(
                f"    schema: {self.schema} \n"
                f"    database: {self.database} \n"
                f"On Databend, database must be omitted or have the same value as"
                f" schema."
            )
        self.database = None

    def _connection_keys(self):
        return (
            "host",
            "port",
            "schema",
            "user",
        )


class DatabendConnectionManager(SQLConnectionManager):
    """
    Databend Connector connection manager.
    """

    TYPE = "databend"

    @contextmanager
    def exception_handler(self, sql):
        try:
            yield
        except mysql.connector.DatabaseError as exc:
            logger.debug("Databend error: {}", str(exc))

            self.release()

            raise dbt.exceptions.RuntimeException(exc) from exc

    @classmethod
    def open(cls, connection):
        if connection.state == "open":
            logger.debug("Connection is already open, skipping open.")
            return connection

        credentials = cls.get_credentials(connection.credentials)

        try:
            connection.handle = mysql.connector.connect(
                host=credentials.host,
                port=credentials.port,
                user=credentials.user,
                password=credentials.password,
            )
            connection.state = "open"
        except mysql.connector.Error as exc:
            logger.debug("Got an error when attempting to open a connection: '{}'", str(exc))

            connection.handle = None
            connection.state = "fail"

            raise dbt.exceptions.FailedToConnectException(str(exc))

        return connection

    def cancel(self, connection):
        connection_name = connection.name
        logger.debug("Cancelling query '{}'", connection_name)
        connection.handle.close()
        logger.debug("Cancel query '{}'", connection_name)

    @classmethod
    def get_credentials(cls, credentials):
        """
        Returns Databend credentials
        """
        return credentials

    @classmethod
    def get_status(cls, _):
        """
        Returns connection status
        """
        return "OK"

    @classmethod
    def get_response(cls, _):
        return "OK"

    def begin(self):
        pass

    def commit(self):
        pass
