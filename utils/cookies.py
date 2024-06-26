from requests import utils as requests_utils

from typing import List
from http.cookiejar import Cookie, CookieJar


def get_cookie_str(cookiejar: CookieJar):

    cookie_str = ''

    for index, c in enumerate(cookiejar):
        cookie_dict = c.__dict__
        cookie_str += f'{cookie_dict['name']}={cookie_dict['value']}' if index == 0 else f';{
            cookie_dict['name']}={cookie_dict['value']}'

    return cookie_str


def get_requests_cookiejar(cookiejar: CookieJar):
    cookies_dict = {}

    for c in cookiejar:
        cookie_dict = c.__dict__
        name = cookie_dict['name']
        value = cookie_dict['value']

        cookies_dict[name] = value

    cookiejar = requests_utils.cookiejar_from_dict(cookies_dict)

    return cookiejar


def update_cookiejar(current_cookiejar: CookieJar, cookies: List[dict]):
    try:
        for c in cookies:
            cookie = Cookie(
                version=0,
                name=c['name'],
                value=c['value'],
                port=c['port'] if 'port' in c else None,
                port_specified=False,
                domain=c['domain'],
                domain_specified=True,
                domain_initial_dot=False,
                path=c['path'] if 'path' in c else None,
                path_specified=True,
                secure=c['secure'] if 'secure' in c else None,
                expires=c['expiry'] if 'expiry' in c else None,
                discard=False,
                comment=None,
                comment_url=None,
                rest=None,
                rfc2109=False
            )

            current_cookiejar.set_cookie(cookie=cookie)

    except Exception as e:
        # TO HANDLE SPECIFIC ERRORS
        print(e)
