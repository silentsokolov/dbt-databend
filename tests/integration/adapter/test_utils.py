from dbt.tests.adapter.utils.test_any_value import BaseAnyValue
from dbt.tests.adapter.utils.test_bool_or import BaseBoolOr
from dbt.tests.adapter.utils.test_cast_bool_to_text import BaseCastBoolToText
from dbt.tests.adapter.utils.test_concat import BaseConcat
from dbt.tests.adapter.utils.test_current_timestamp import BaseCurrentTimestampNaive
from dbt.tests.adapter.utils.test_date_trunc import BaseDateTrunc
from dbt.tests.adapter.utils.test_dateadd import BaseDateAdd
from dbt.tests.adapter.utils.test_datediff import BaseDateDiff
from dbt.tests.adapter.utils.test_escape_single_quotes import BaseEscapeSingleQuotesQuote
from dbt.tests.adapter.utils.test_except import BaseExcept
from dbt.tests.adapter.utils.test_hash import BaseHash
from dbt.tests.adapter.utils.test_intersect import BaseIntersect
from dbt.tests.adapter.utils.test_last_day import BaseLastDay
from dbt.tests.adapter.utils.test_length import BaseLength
from dbt.tests.adapter.utils.test_position import BasePosition
from dbt.tests.adapter.utils.test_replace import BaseReplace
from dbt.tests.adapter.utils.test_right import BaseRight
from dbt.tests.adapter.utils.test_safe_cast import BaseSafeCast
from dbt.tests.adapter.utils.test_split_part import BaseSplitPart
from dbt.tests.adapter.utils.test_string_literal import BaseStringLiteral
from pytest import mark


class TestAnyValue(BaseAnyValue):
    pass


@mark.skip("Not func BoolOr")
class TestBoolOr(BaseBoolOr):
    pass


@mark.skip("Bool cast to int, not true / false")
class TestCastBoolToText(BaseCastBoolToText):
    pass


@mark.skip("Not func DateAdd")
class TestDateAdd(BaseDateAdd):
    pass


@mark.skip("Not func DateTrunc")
class TestBaseDateTrunc(BaseDateTrunc):
    pass


@mark.skip("Not support ||")
class TestConcat(BaseConcat):
    pass


@mark.skip("Not func DateDiff")
class TestDateDiff(BaseDateDiff):
    pass


@mark.skip("Not support")
class TestEscapeSingleQuotes(BaseEscapeSingleQuotesQuote):
    pass


class TestCurrentTimestampNaive(BaseCurrentTimestampNaive):
    pass


@mark.skip("Not support")
class TestExcept(BaseExcept):
    pass


@mark.skip("Not support")
class TestHash(BaseHash):
    pass


@mark.skip("Not support")
class TestIntersect(BaseIntersect):
    pass


@mark.skip("Not func dateadd")
class TestLastDay(BaseLastDay):
    pass


class TestLength(BaseLength):
    pass


class TestBasePosition(BasePosition):
    pass


@mark.skip("Work! Skip because NOT NULL is dafault")
class TestBaseReplace(BaseReplace):
    pass


@mark.skip("Work! Skip because NOT NULL is dafault")
class TestBaseRight(BaseRight):
    pass


@mark.skip("Not support")
class TestBaseSafeCast(BaseSafeCast):
    pass


@mark.skip("Not func split_part")
class TestBaseSplitPart(BaseSplitPart):
    pass


class TestBaseStringLiteral(BaseStringLiteral):
    pass
