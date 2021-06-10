import string

import pytest
from faker import Faker

from api.test_api.base import ApiBase
from db.mysql.models import User
import random

fake = Faker()

@pytest.mark.API
class TestApi(ApiBase):

    def test_create_user_correct(self):
        """
        Проверяем создание пользователя, когда все параметры корректные
        Шаги: собираем фейковые данные, отправляем.
        Ожидается: запись в БД создана
        """
        self.api_client.post_login("ruslan", "123456")
        first = fake.first_name()
        last = fake.last_name()[:15 - len(first)]
        username = first + " " + last
        email = fake.email()
        password = "xxx()J@#(#@JT"
        self.api_client.post_register(username, password, email, need_status=210)
        last_user = self.mysql.session.query(User).order_by(-User.id).first()
        self.api_client.session.cookies.clear()
        assert last_user.username == username


    def test_shortlogin_user_add(self):
        self.api_client.post_login("ruslan", "123456")
        username = str(random.randint(1001, 9999))
        email = fake.email()
        password = "90u3093ugn-n3ug23"
        reg_res = self.api_client.post_register(username, password, email, need_status=400)
        assert reg_res.status_code == 400
        self.api_client.session.cookies.clear()

    def test_user_add_incorrect_email(self):
        self.api_client.post_login("ruslan", "123456")
        first = fake.first_name()
        last = fake.last_name()[:15 - len(first)]
        username = first + " " + last
        email = "bademail"
        password = "xxx()J@#(#@JT"
        reg_res = self.api_client.post_register(username, password, email, need_status=400)
        assert reg_res.result.lower() != "user was added!"
        self.api_client.session.cookies.clear()

    def test_user_add_short_email(self):
        self.api_client.post_login("ruslan", "123456")
        first = fake.first_name()
        last = fake.last_name()[:15 - len(first)]
        username = first + " " + last
        email = "bad"
        password = "xxx()J@#(#@JT"
        reg_res = self.api_client.post_register(username, password, email, need_status=400)
        assert reg_res.result.lower() != "user was added!"
        self.api_client.session.cookies.clear()

    def test_login(self):
        self.api_client.session.cookies.clear()
        res = self.api_client.post_login('ruslan', '123456')
        assert "Test Server | Welcome!" in res.text

    def test_ban_user(self):
        self.api_client.session.cookies.clear()
        self.api_client.post_login('ruslan', '123456')
        first = fake.first_name()
        last = fake.last_name()[:15-len(first)]
        username = first+" "+last
        email = fake.email()
        password = "xxx()J@#(#@JT"
        self.api_client.post_register(username, password, email, need_status=210)
        self.api_client.get_block_user(username)
        self.mysql.session.commit()
        self.mysql.session.expire_all()
        this_user = self.mysql.session.query(User).filter(User.username==username, User.email==email).first()
        assert this_user.access == 0

    def test_unban_user(self):
        self.api_client.session.cookies.clear()
        self.api_client.post_login('ruslan', '123456')
        first = fake.first_name()
        last = fake.last_name()[:15 - len(first)]
        username = first + " " + last
        email = fake.email()
        password = "xxx()J@#(#@JT"
        self.api_client.post_register(username, password, email, need_status=210)
        self.api_client.get_block_user(username)
        self.mysql.session.commit()
        self.mysql.session.expire_all()
        this_user = self.mysql.session.query(User).filter(User.username == username, User.email == email).first()
        assert this_user.access == 0
        self.api_client.get_unblock_user(username)
        self.mysql.session.commit()
        #self.mysql.session.expire(last_user)
        self.mysql.session.refresh(this_user)
        this_user = self.mysql.session.query(User).filter(User.username == username, User.email == email).first()
        assert this_user.access == 1

    def test_del_user(self):
        self.api_client.session.cookies.clear()
        self.api_client.post_login('ruslan', '123456')
        last_user = self.mysql.session.query(User).order_by(-User.id).first()
        name = last_user.username
        email = last_user.email
        self.api_client.get_del_user(name)
        self.mysql.session.commit()
        self.mysql.session.expire_all()
        last_user = self.mysql.session.query(User).filter(User.username==name, User.email==email).all()
        #assert (name != last_user.username and email != last_user.email)
        assert len(last_user)==0

    def test_repeat_user_add(self):
        self.api_client.post_login("ruslan", "123456")
        last_user = self.mysql.session.query(User).order_by(-User.id).first()
        email = fake.email()
        password = "xxx()J@#(#@JT"
        reg_res = self.api_client.post_register(last_user.username, password, email, need_status=304)
        assert reg_res.status_code == 304
        self.api_client.session.cookies.clear()

    def test_repeat_email(self):
        self.api_client.post_login("ruslan", "123456")
        last_user = self.mysql.session.query(User).order_by(-User.id).first()
        first = fake.first_name()
        last = fake.last_name()[:15 - len(first)]
        username = first + " " + last
        password = "xxx()J@#(#@JT"
        reg_res = self.api_client.post_register(username, password, last_user.email, need_status=304)
        assert reg_res.status_code == 304
        self.api_client.session.cookies.clear()

    def test_long_username(self):
        self.api_client.post_login("ruslan", "123456")
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))
        email = fake.email()
        password = "xxx()J@#(#@JT"
        reg_res = self.api_client.post_register(username, password, email, need_status=400)
        assert reg_res.status_code == 400
        self.api_client.session.cookies.clear()