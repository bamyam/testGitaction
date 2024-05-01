from pydantic import BaseModel

class Location(BaseModel):
    location: str
    security_grade: int

    class Config:
        from_attributes = True