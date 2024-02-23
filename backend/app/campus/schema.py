from app.core.types import MongoModel, MongoListModel, PydanticObjectId


class CampusSchema(MongoModel):
    id: PydanticObjectId
    name: str

    class Config:
        orm_mode = True


class CampusListSchema(MongoListModel):
    __root__: list[CampusSchema]

    class Config:
        orm_mode = True
