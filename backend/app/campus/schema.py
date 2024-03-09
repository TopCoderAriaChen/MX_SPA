from app.core.types import MongoListModel, MongoModel, PydanticObjectId


class CampusSchema(MongoModel):
    id: PydanticObjectId
    name: str


class CampusListSchema(MongoListModel):
    __root__: list[CampusSchema]
