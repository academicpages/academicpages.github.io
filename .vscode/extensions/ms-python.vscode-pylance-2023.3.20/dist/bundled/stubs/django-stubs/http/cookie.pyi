from http.cookies import SimpleCookie as SimpleCookie
from typing import Dict

def parse_cookie(cookie: str) -> Dict[str, str]: ...
