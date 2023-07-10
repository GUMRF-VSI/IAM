from fastapi import HTTPException, status


class TokenException:
    __unknown_token_message = 'Unknown token'
    __invalid_token_message = 'Invalid token'
    __token_expired = 'Token expired.'

    @property
    def unknown_token(self):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__unknown_token_message)

    @property
    def invalid_token(self):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.__invalid_token_message)

    @property
    def token_expired(self):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.__token_expired)


token = TokenException()
