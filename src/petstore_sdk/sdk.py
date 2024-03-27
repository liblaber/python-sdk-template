from .services.pets import PetsService
from .net.environment import Environment


class PetstoreSdk:
    def __init__(self, access_token: str, base_url: str = Environment.DEFAULT.value):
        """
        Initializes PetstoreSdk the SDK class.
        """
        self.pets = PetsService(base_url=base_url)
        self.set_access_token(access_token)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.pets.set_base_url(base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.pets.set_access_token(access_token)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
