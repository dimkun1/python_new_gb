# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import re
import pytest
from os import path
from Project import Project
from User import User
import Excep as Ex

@pytest.fixture
def project():
    return Project.load_users('users.json')

@pytest.fixture
def admin(project):
    project.enter('Sam', 114)
    return project.admin

def test_enter(project):
    project.enter('Han', 105)
    assert project.admin.name == 'Han' and \
            project.admin.uid == 105

def test_enter_error(project):
    with pytest.raises(Ex.ErrorAcsess, match="Пользователя Иван с ID-10 не существует!"):
        project.enter('Иван', 10)

def test_add_user(project, admin):
    new_user = User('Иван', 105, 7)
    project.add_user('Иван', 105, 7)
    assert new_user in project.users

def test_add_user_error_level(project, admin):
    with pytest.raises(Ex.ErrorLevel, match=re.escape("Операция для пользователя Иван не может быть выполнена, \
т.к. его уровень доступа (1) выше, чем уровень администратора (4)!")):
        project.add_user('Иван', 105, 1)

def test_add_user_error_user(project, admin):

    with pytest.raises(Ex.ErrorUser, match="Пользователь Carl с ID-106 уже существует!"):
        project.add_user('Carl', 106, 6)

def test_del_user(project, admin):
    new_user = User('Han', 105, 5)
    project.del_user('Han', 105)
    assert not new_user in project.users

def test_del_user_error_user(project, admin):
    with pytest.raises(Ex.ErrorAcsess, match="Пользователя Иван с ID-105 не существует!"):
        project.del_user('Иван', 105)

def test_del_user_error_level(project, admin):
    with pytest.raises(Ex.ErrorLevel, match=re.escape("Операция для пользователя Lee не может быть выполнена, \
т.к. его уровень доступа (1) выше, чем уровень администратора (4)!")):
        project.del_user('Lee', 104)

def test_file_not_exist(project, tmp_path):
    f_name = tmp_path / 'result.json'
    project.write_to_json(f_name)
    assert path.exists(f_name) == True and path.getsize(f_name) != 0


if __name__ == '__main__':
    pytest.main(['-v'])