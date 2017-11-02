from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from .models import Personil


class MongoTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def get_model(self):
        return Personil

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.get(token=key)

        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return token, token.token
