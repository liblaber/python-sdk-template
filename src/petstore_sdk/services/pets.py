from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.pet import Pet


class PetsService(BaseService):

    @cast_models
    def list_pets(self, limit: int = None) -> List[Pet]:
        """list_pets

        :param limit: How many items to return at one time (max 100), defaults to None
        :type limit: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A paged array of pets
        :rtype: List[Pet]
        """

        Validator(int).is_optional().max(100).validate(limit)

        serialized_request = (
            Serializer(f"{self.base_url}/pets", self.get_default_headers())
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [Pet._unmap(item) for item in response]

    @cast_models
    def create_pets(self, request_body: Pet):
        """create_pets

        :param request_body: The request body.
        :type request_body: Pet
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(Pet).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/pets", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def show_pet_by_id(self, pet_id: str) -> Pet:
        """show_pet_by_id

        :param pet_id: The id of the pet to retrieve
        :type pet_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Expected response to a valid request
        :rtype: Pet
        """

        Validator(str).validate(pet_id)

        serialized_request = (
            Serializer(f"{self.base_url}/pets/{{petId}}", self.get_default_headers())
            .add_path("petId", pet_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Pet._unmap(response)
