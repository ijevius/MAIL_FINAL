import pytest

from db.mysql.builder import MySQLBuilder

class ApiBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, logger, api_client, mysql_client):
        self.config = config
        self.logger = logger
        self.logger.debug('Initial setup done!')
        self.api_client = api_client
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)
        self.prepare()