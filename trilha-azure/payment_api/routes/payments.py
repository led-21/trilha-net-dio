from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.payment import PaymentCreate, PaymentInDB, PaymentUpdate, PaymentStatus
from app.models.payment import Payment
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.post("/payments/", response_model=PaymentInDB, status_code=status.HTTP_201_CREATED)
async def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Cria um novo pagamento.
    - Valida o token do cartão
    - Processa o pagamento com o gateway (ex: Azure Payment HSM)
    - Registra a transação no banco de dados
    """
    # Simulação de processamento de pagamento
    transaction_id = f"tx_{current_user}_{int(datetime.now().timestamp())}"
    
    # Em produção, use Azure Payment HSM para processamento seguro
    db_payment = Payment(
        amount=payment.amount,
        currency=payment.currency,
        description=payment.description,
        payment_method=payment.payment_method,
        customer_id=payment.customer_id,
        transaction_id=transaction_id,
        card_last_four=payment.card_token[-4:],  # Simulação
        card_brand="visa"  # Simulação
    )
    
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    
    return db_payment

@router.get("/payments/", response_model=List[PaymentInDB])
async def read_payments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Lista pagamentos (acesso restrito)
    """
    payments = db.query(Payment).offset(skip).limit(limit).all()
    return payments

@router.get("/payments/{payment_id}", response_model=PaymentInDB)
async def read_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Obtém detalhes de um pagamento específico
    """
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.put("/payments/{payment_id}", response_model=PaymentInDB)
async def update_payment_status(
    payment_id: int,
    payment_update: PaymentUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    """
    Atualiza o status de um pagamento (apenas admin)
    """
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    payment.status = payment_update.status
    db.commit()
    db.refresh(payment)
    
    return payment
