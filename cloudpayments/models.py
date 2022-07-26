from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Any

from cloudpayments.enums import CurrencyCode


@dataclass
class PaymentPayer:
    city: str
    birth: str
    phone: str
    street: str
    address: str
    country: str
    post_code: str
    last_name: str
    first_name: str
    middle_name: str


@dataclass
class PaymentRequest:
    amount: float
    ip_address: str
    card_cryptogram_packet: str
    name: Optional[str] = None
    email: Optional[str] = None
    payer: Optional[PaymentPayer] = None
    account_id: Optional[str] = None
    invoice_id: Optional[str] = None
    payment_url: Optional[str] = None
    description: Optional[str] = None
    culture_name: Optional[str] = None
    json_data: Optional[dict] = None
    currency: Optional[CurrencyCode] = CurrencyCode.RUB


@dataclass
class PaymentResponse:
    success: bool
    message: str
    model: Optional[Any] = None
