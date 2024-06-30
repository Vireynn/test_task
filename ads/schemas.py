from pydantic import BaseModel, Field, ConfigDict

class AdvertSchema(BaseModel):
    advert_id: int = Field(..., description="ID объявления")
    title: str = Field(..., description="Заголовок объявления")
    author: str = Field(..., description="Автор объявления")
    views: int = Field(..., description="Количество просмотров")
    position: int = Field(..., description="Позиция объявления")

class AdvertCreate(AdvertSchema):
    pass

class Advert(AdvertSchema):
    model_config = ConfigDict(from_attributes=True)
