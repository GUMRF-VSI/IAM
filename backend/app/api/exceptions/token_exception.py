from fastapi import HTTPException, status


class TokenException:
    unknown_token_message = 'Unknown token'
    invalid_token_message = 'Invalid token'

    @property
    def unknown_token(self):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.unknown_token_message)

    @property
    def invalid_token(self):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.invalid_token_message)


token = TokenException()
