from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat

from enums import TransactionType


class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: PositiveFloat
    timestamp: AwareDatetime | NaiveDatetime