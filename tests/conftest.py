import pytest

@pytest.fixture()
def delete_param(param):

    yield

    del param['sign']