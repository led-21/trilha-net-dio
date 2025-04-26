from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class PaymentStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    refunded = "refunded"

class PaymentBase(BaseModel):
    amount: float = Field(..., gt=0, description="O valor deve ser maior que zero")
    currency: str = "BRL"
    description: Optional[str] = None

class PaymentCreate(PaymentBase):
    payment_method: str
    customer_id: str
    card_token: str  # Tokenizado pelo frontend (PCI compliance)

class PaymentUpdate(BaseModel):
    status: Optional[PaymentStatus] = None

class PaymentInDB(PaymentBase):
    id: int
    status: PaymentStatus
    created_at: datetime
    updated_at: datetime
    transaction_id: str
    card_last_four: str
    card_brand: str
    
    class Config:
        orm_mode = True
