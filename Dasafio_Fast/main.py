from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from controllers import account, auth, transaction
from database import database, engine, metadata
from exceptions import AccountNotFoundError, BusinessError


@asynccontextmanager
async def lifespan(app: FastAPI):
    metadata.create_all(engine)  
    await database.connect()
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Operations for authentication.",
    },
    {
        "name": "account",
        "description": "Operations to maintain accounts.",
    },
    {
        "name": "transaction",
        "description": "Operations to maintain transactions.",
    },
]

app = FastAPI(
    title="API de Transações",
    version="1.0.0",
    summary="Microsserviço para gerenciar operações de saque e depósito em contas correntes.",
    description="""
    A API de Transações é um microsserviço responsável pelo registro de transações realizadas em contas correntes. 💸💰


    ## Contas


    * **Criar contas**.
    * **Listar contas**.
    * **Listar transações de uma conta por ID**.


    ## Transações


    * **Criar transações**.
    """,
    openapi_tags=tags_metadata,
    redoc_url=None,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])


@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(request: Request, exc: AccountNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Account not found."},
    )


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": str(exc)},
    )