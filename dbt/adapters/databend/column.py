from dataclasses import dataclass
from typing import Any, TypeVar

from dbt.adapters.base.column import Column
from dbt.exceptions import RuntimeException

Self = TypeVar("Self", bound="DatabendColumn")


@dataclass
class DatabendColumn(Column):
    def __repr__(self) -> str:
        return f"<DatabendColumn {self.name} ({self.data_type})>"

    def is_string(self) -> bool:
        return self.dtype.lower() in [
            "string",
            "varchar",
        ]

    def is_integer(self) -> bool:
        return self.dtype.lower().startswith("int") or self.dtype.lower() in (
            "tinyint",
            "smallint",
            "bigint",
        )

    def is_numeric(self) -> bool:
        return False

    def is_float(self) -> bool:
        return self.dtype.lower() in ("float", "double")

    def string_size(self) -> int:
        if not self.is_string():
            raise RuntimeException("Called string_size() on non-string field!")

        if self.char_size is None:
            return 256
        else:
            return int(self.char_size)

    @classmethod
    def string_type(cls, size: int) -> str:
        return "VARCHAR"

    @classmethod
    def numeric_type(cls, dtype: str, precision: Any, scale: Any) -> str:
        return dtype

    def literal(self, value):
        return f"CAST({value} AS {self.dtype})"

    def can_expand_to(self, other_column: "Column") -> bool:
        return self.is_string() and other_column.is_string()
