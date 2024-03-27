from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class Pet(BaseModel):
    """Pet

    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    :param tag: tag, defaults to None
    :type tag: str, optional
    """

    def __init__(self, id_: int, name: str, tag: str = None):
        self.id_ = id_
        self.name = name
        if tag is not None:
            self.tag = tag
