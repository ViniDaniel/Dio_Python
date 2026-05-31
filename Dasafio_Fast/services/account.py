from databases.interfaces import Record

from database import database
from models.account import accounts
from auth.account import AccountIn
from security import hash_password


class AccountService:
    async def read_all(self, limit: int = 10, skip: int = 0) -> list[Record]:
        query = accounts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)


    async def get_by_username(self, username: str) -> Record | None:
        query = accounts.select().where(accounts.c.username == username)
        return await database.fetch_one(query)


    async def create(self, account: AccountIn) -> Record:
        command = accounts.insert().values(
            user_id=account.user_id,
            username=account.username,
            hashed_password=hash_password(account.password),
            balance=0,
        )
        account_id = await database.execute(command)

        query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(query)