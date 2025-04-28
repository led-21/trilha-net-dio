from pydantic import BaseModel

class Car(BaseModel):
    model: str
    brand: str
    year: int
    price_per_day: float
    available: bool = True
