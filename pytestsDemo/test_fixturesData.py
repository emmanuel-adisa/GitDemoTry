import pytest

@pytest.mark.usefixtures("dataLoad")
class Testexample2:
    def test_editProfile(self,dataLoad):
        print(dataLoad[0])
        print(dataLoad[2])
