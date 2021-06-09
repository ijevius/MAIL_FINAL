import json
import logging
import requests

logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 50000 #??? default 500


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        #self.post_login('r.iudin@internet.ru', '#@_J)#@_)I#Gg')

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True, json=None,
                 files=None, allow_redirects=True):
        url = location

        self.log_pre(method, url, headers, data, expected_status)
        self.session.max_redirects = 100

        response = self.session.request(method, url, headers=headers, data=data, json=json, files=files, allow_redirects=allow_redirects)

        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.\n'
                                              f'Message: {response.text}')

        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response.get('bErrorMsg', 'Unknown')
                raise ResponseErrorException(f'Request "{url}" return error "{error}"!')
            return json_response

        return response

    @property
    def post_headers(self):
        return {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    def post_login(self, user, password):
        self.session.cookies.clear()
        location = 'http://0.0.0.0:81/login'

        data = {
            'username': user,
            'password': password,
            'submit': 'Login'
        }
        result = self._request('POST', location, data=data, jsonify=False)
        return result

    def post_register(self, user, password, email, need_status):
        location = 'http://0.0.0.0:81/api/add_user'

        data = {
            'username': user,
            'email': email,
            'password': password
        }
        result = self._request('POST', location, json=data, jsonify=False,
                               expected_status=need_status)

        return result

    def get_logout(self):
        location = 'http://0.0.0.0:81/logout'
        result = self._request('POST', location, jsonify=False)

        return result

    def get_block_user(self, username):
        location = f'http://0.0.0.0:81/api/block_user/{username}'
        result = self._request('GET', location, jsonify=False)

        return result

    def get_unblock_user(self, username):
        location = f'http://0.0.0.0:81/api/accept_user/{username}'
        result = self._request('GET', location, jsonify=False)

        return result

    def get_del_user(self, username):
        location = f'http://0.0.0.0:81/api/del_user/{username}'
        result = self._request('GET', location, jsonify=False, expected_status=204)

        return result
