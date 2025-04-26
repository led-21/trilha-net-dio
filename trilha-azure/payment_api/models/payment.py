from sqlalchemy import Column, String, Integer, Float, DateTime, Enum
from app.db.session import Base
import enum
from datetime import datetime

class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="BRL")
    description = Column(String(255))
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    payment_method = Column(String(50))
    customer_id = Column(String(100))
    transaction_id = Column(String(100), unique=True)
    
    # Campos para PCI compliance (armazenar de forma segura usando Azure Key Vault)
    card_last_four = Column(String(4))
    card_brand = Column(String(20))
    
    def __repr__(self):
        return f"<Payment {self.transaction_id}>"
