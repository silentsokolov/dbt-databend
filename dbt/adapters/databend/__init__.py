from dbt.adapters.base import AdapterPlugin

from dbt.adapters.databend.column import DatabendColumn  # noqa
from dbt.adapters.databend.connections import DatabendConnectionManager, DatabendCredentials  # noqa
from dbt.adapters.databend.impl import DatabendAdapter
from dbt.adapters.databend.relation import DatabendRelation  # noqa
from dbt.include import databend  # noqa

Plugin = AdapterPlugin(
    adapter=DatabendAdapter,
    credentials=DatabendCredentials,
    include_path=databend.PACKAGE_PATH,
)
