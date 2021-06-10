import pytest
from faker import Faker

from db.mysql.builder import MySQLBuilder
from db.mysql.models import User

fake = Faker()

class ApiBase:

    def prepare(self):
        x = self.mysql.session.query(User).filter(User.username == 'ruslan', User.password == '123456').first()
        if x==None:
            user = User(username="ruslan",
                             password='123456',
                             email='testemail@mail.ru',
                        access=1, active=0)

            self.mysql.session.add(user)
            self.mysql.session.commit()
        for _ in range(10):
            self.api_client.post_login("ruslan", "123456")
            first = fake.first_name()
            last = fake.last_name()[:15 - len(first)]
            username = first + " " + last
            email = fake.email()
            password = "xxx()J@#(#@JT"
            self.api_client.post_register(username, password, email, need_status=210)


    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, logger, api_client, mysql_client):
        self.config = config
        self.logger = logger
        self.logger.debug('Initial setup done!')
        self.api_client = api_client
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)
        self.prepare()