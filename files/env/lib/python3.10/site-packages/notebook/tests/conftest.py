def pytest_addoption(parser):
    parser.addoption('--integration_tests', action='store_true', dest="integration_tests",
                 default=False, help="enable integration tests")

def pytest_configure(config):
    if not config.option.integration_tests:
        setattr(config.option, 'markexpr', 'not integration_tests')
