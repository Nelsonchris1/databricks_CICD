# from test_dabs.main import get_taxis, get_spark
import pytest


# def test_main():
#     taxis = get_taxis(get_spark())
#     assert taxis.count() > 5


@pytest.fixture(scope="module")
def environment(pytestconfig):
    return pytestconfig.getoption("environment")

def test_environmentvariable(environment):
    assert environment == "dev"


class GetVariables:
    
    def list_lenght(self):
        return [0, 2, 4, 6, 8]


# @pytest.fixture(scope="module")
# def environment(request):
#     return request.config.getoption("--environment")



# def test_shouldpass():
#     assert True

# def test_shouldfail():
#     assert False




def test_list():
    gv = GetVariables()
    assert len(gv.list_lenght()) < 10 # Check if list length is less than 10
    assert all(num % 2 == 0 for num in gv.list_lenght())
