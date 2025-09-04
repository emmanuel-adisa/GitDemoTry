# Any pytest file should start with test_ or end with _test
#pytest method names should always start with test
#any code should be wrapped in method only
#method name should make sense
# -k stands for method names execution, -s logs in output -v stands for more info metadata
#you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail run test but because I know it will fail it won't be added to the report
#fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixture
#and makes it available to all test cases (fixture name in parameters of method)
#data driven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello" #operation
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


@pytest.fixture()
def setup():
    print("I will be executed first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")