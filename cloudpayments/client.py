from dataclasses import asdict
from logging import getLogger
from typing import Dict, Any

import humps
from aiohttp import BasicAuth

from cloudpayments.models import PaymentRequest, PaymentResponse
from interaction.client import AbstractInteractionClient

_logger = getLogger(__name__)


class CloudPaymentsClient(AbstractInteractionClient):
    SERVICE = "cloudpayments"
    BASE_URL = "https://api.cloudpayments.ru/"
    CONNECTOR = None

    def __init__(self, public_id: str) -> None:
        super().__init__()
        self._public_id = public_id

    def _get_session_kwargs(self) -> Dict[str, Any]:
        kwargs = super()._get_session_kwargs()
        kwargs["auth"] = BasicAuth(self._public_id)
        return kwargs

    async def crypto_sms_payment(self, data: PaymentRequest) -> PaymentResponse:
        """
        Одностадийная оплата по криптограмме
        :param data: запрос об оплате
        :return: ответ оператора
        """
        body = humps.pascalize(asdict(data))
        response = await self.post("charge", self.endpoint_url("/payments/charge"), json=body)
        return PaymentResponse(**humps.depascalize(response))
