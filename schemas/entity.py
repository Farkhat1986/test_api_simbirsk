from typing import List, Optional
from pydantic import BaseModel, Field, validator

class Addition(BaseModel):
    additional_info: str
    additional_number: int
    id: Optional[int] = None

    @validator('additional_number')
    def validate_additional_number(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("дополнительное число должно быть в диапазоне от 0 до 100")
        return v

class EntityResponse(BaseModel):
    id: int
    important_numbers: List[int] = Field(..., min_items=1, max_items=5)
    title: str
    verified: bool
    addition: Addition

    @validator('important_numbers.*')
    def validate_important_numbers(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("все важные числа должны быть в диапазоне от 0 до 10")
        return v

class EntityCreateRequest(BaseModel):
    important_numbers: List[int] = Field(..., min_items=1, max_items=5)
    title: str
    verified: bool
    addition: Addition

class EntityUpdateRequest(BaseModel):
    important_numbers: Optional[List[int]] = Field(None, min_items=1, max_items=5)
    title: Optional[str]
    verified: Optional[bool]
    addition: Optional[Addition]