from pydantic import AwareDatetime, BaseModel, NaiveDatetime


class AccountOut(BaseModel):
    id: int
    user_id: int
    username: str
    balance: float
    created_at: AwareDatetime | NaiveDatetime