from pytest import Pytester
from pytest import ExitCode


def test_asserto_fixture(pytester: Pytester) -> None:
    pytester.makepyfile(
        """
        from asserto import Asserto
        def test_fixture(asserto):
            asserto(asserto).is_instance(Asserto)
        """
    )
    result = pytester.runpytest()
    assert result.ret == ExitCode.OK
