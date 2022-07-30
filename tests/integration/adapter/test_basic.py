from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests


class TestBaseSimpleMaterializations(BaseSimpleMaterializations):
    pass


class TestEmpty(BaseEmpty):
    pass


class TestGenericTests(BaseGenericTests):
    pass


class TestSingularTests(BaseSingularTests):
    pass
