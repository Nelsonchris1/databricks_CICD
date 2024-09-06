def pytest_addoption(parser):
    parser.addoption("--environment", action="store", help="Specify environment:dev, stage, prod")
