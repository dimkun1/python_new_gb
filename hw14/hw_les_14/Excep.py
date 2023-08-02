# Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class BaseException(Exception):
    def __init__(self, user) -> None:
        self.user = user

    def __str__(self) -> str:
        return f"Пользователь {self.user.name} не может быть задействован в данной операции!"


class ErrorAcsess(BaseException):
    def __init__(self, name, uid) -> None:
        self.name = name
        self.uid = uid

    def __str__(self) -> str:
        return f"Пользователя {self.name} с ID-{self.uid} не существует!"


class ErrorLevel(BaseException):
    def __init__(self, name, level, admin) -> None:
        self.name = name
        self.level = level
        self.admin = admin

    def __str__(self) -> str:
        return f"Операция для пользователя {self.name} не может быть выполнена, \
т.к. его уровень доступа ({self.level}) выше, чем уровень администратора ({self.admin.level})!"


class ErrorUser(BaseException):
    def __init__(self, name, uid) -> None:
        self.name = name
        self.uid = uid

    def __str__(self) -> str:
        return f"Пользователь {self.name} с ID-{self.uid} уже существует!"