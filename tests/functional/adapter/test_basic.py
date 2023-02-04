import pytest
from dbt.tests.adapter.basic.expected_catalog import (
    base_expected_catalog,
    expected_references_catalog,
    no_stats,
)
from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_docs_generate import BaseDocsGenerate, BaseDocsGenReferences
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_validate_connection import BaseValidateConnection
from pytest import mark


class TestBaseSimpleMaterializations(BaseSimpleMaterializations):
    pass


class TestEmpty(BaseEmpty):
    pass


@mark.skip("Not support ALTER")
class TestIncremental(BaseIncremental):
    pass


@mark.skip("Not support ALTER")
class TestSnapshotTimestamp(BaseSnapshotTimestamp):
    pass


@mark.skip("Not support ALTER")
class TestSnapshotCheckCols(BaseSnapshotCheckCols):
    pass


class TestGenericTests(BaseGenericTests):
    pass


class TestSingularTests(BaseSingularTests):
    pass


class TestValidateConnection(BaseValidateConnection):
    pass


# @mark.skip("Need fix https://github.com/datafuselabs/databend/issues/6922")
class TestDocsGenerate(BaseDocsGenerate):
    @pytest.fixture(scope="class")
    def expected_catalog(self, project, profile_user):
        return base_expected_catalog(
            project,
            role=None,
            id_type="INTEGER",
            text_type="VARCHAR",
            time_type="timestamp",
            view_type="view",
            table_type="table",
            model_stats=no_stats(),
        )


# @mark.skip("Need fix https://github.com/datafuselabs/databend/issues/6922")
class TestDocsGenReferences(BaseDocsGenReferences):
    @pytest.fixture(scope="class")
    def expected_catalog(self, project, profile_user):
        return expected_references_catalog(
            project,
            role=None,
            id_type="INTEGER",
            text_type="VARCHAR",
            time_type="timestamp",
            view_type="view",
            table_type="table",
            model_stats=no_stats(),
            bigint_type="BIGINT",
        )
