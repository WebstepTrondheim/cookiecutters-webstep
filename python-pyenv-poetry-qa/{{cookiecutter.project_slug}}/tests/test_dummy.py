from {{ cookiecutter.package_slug }} import make_pytest_happy


def test_dummy():
    assert make_pytest_happy() == True
