import sqlalchemy as sa

from database import metadata


accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.Integer, nullable=False, index=True, unique=True),
    sa.Column("username", sa.String(50), nullable=False, unique=True),
    sa.Column("hashed_password", sa.String(255), nullable=False),
    sa.Column("balance", sa.Numeric(10, 2), nullable=False, server_default="0"),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now()),
)