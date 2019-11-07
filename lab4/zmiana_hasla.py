# zmiana hasla  dla danego uzytkownika
import crypt
import os
import htpasswd
from typing import Tuple, List


def parse_htpasswd(file_name: str) -> List[Tuple[str, ...]]:
    results = []
    with open(file_name) as file:
        for line in file:
            results.append(tuple(line.strip().split(':')))
    return results


def is_user_in_base(file_name: str, name: str, password: str) -> bool:
    data = parse_htpasswd(file_name)
    user = next((u for u in data if u[0] == name), None)
    if user is None:
        return False
    hash = user[1]
    salt = hash[:2]
    return crypt.crypt(password, salt) == hash


def create_file():
    file_name = '.htpasswd'
    if os.path.exists(file_name):
        return file_name
    open(file_name, 'a').close()
    users = [('Adam', 'haslo'), ('Steve', 'Rogers'), ('Tony', 'haslo')]
    with htpasswd.Basic(file_name) as userdb:
        for user in users:
            userdb.add(*user)
    return file_name


if __name__ == '__main__':
    htpasswd_file = create_file()
    user_name = input('Enter user name: ')
    old_password = input('Enter old password: ')
    if not is_user_in_base(htpasswd_file, user_name, old_password):
        print('Wrong username or password')
    else:
        with htpasswd.Basic(htpasswd_file) as userdb:
            new_password = input('Enter new password: ')
            userdb.change_password(user_name, new_password)
