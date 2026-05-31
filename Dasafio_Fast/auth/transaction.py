from pydantic import BaseModel, PositiveFloat

from enums import TransactionType


class TransactionIn(BaseModel):
    model_config = {"use_enum_values": True}

    account_id: int
    type: TransactionType
    amount: PositiveFloat