# Any pytest file should start with test_ or end with _test
#pytest method names should always start with test
#any code should be wrapped in method only
#method name should make sense
# -k stands for method names execution, -s logs in output -v stands for more info metadata
#you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail run test but because I know it will fail it won't be added to the report
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])