from fastapi import Depends, FastAPI, Header, HTTPException

from api import users#, products, token, salesdatas, salestemps 

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(token.router, prefix="/token", tags=["token"])
# app.include_router(products.router, prefix="/products", tags=["products"])
# app.include_router(salestemps.router, prefix="/salestemps", tags=["salestemps"])
# app.include_router(salesdatas.router, prefix="/salesdatas", tags=["salesdatas"])