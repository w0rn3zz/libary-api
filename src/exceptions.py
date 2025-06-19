from fastapi import HTTPException, status


class LibaryAPIException(HTTPException):
    status_code = 500
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(LibaryAPIException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"
        
class IncorrectEmailOrPasswordException(LibaryAPIException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"
        
class TokenExpiredException(LibaryAPIException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Срок действия токена истек"
        
class TokenAbsentException(LibaryAPIException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"
        
class IncorrectTokenFormatException(LibaryAPIException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"
        
class UserIsNotPresentException(LibaryAPIException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail = 'Пользователь не найден'