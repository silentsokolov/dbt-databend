import os

import pytest

# Import the standard integration fixtures as a plugin
# Note: fixtures with session scope need to be local
pytest_plugins = ["dbt.tests.fixtures.project"]


# The profile dictionary, used to write out profiles.yml
# dbt will supply a unique schema per test, so we do not specify 'schema' here
@pytest.fixture(scope="class")
def dbt_profile_target():
    return {
        "type": "databend",
        "port": int(os.environ.get("PORT_ENV_VAR_NAME", 3307)),
        "host": os.environ.get("HOST_ENV_VAR_NAME", "0.0.0.0"),
        "user": os.environ.get("USER_ENV_VAR_NAME", "root"),
        "password": os.environ.get("PASSWORD_ENV_VAR_NAME", ""),
    }
