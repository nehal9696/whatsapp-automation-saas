from fastapi import FastAPI
from app.api.business import router as business_router
from app.db.init_db import init_db
from app.api.message import router as message_router
from app.api.auth import router as auth_router
from app.api.webhook import router as webhook_router
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.rate_limiter import limiter

app = FastAPI()

app.state.limiter = limiter

# CREATE TABLES ON STARTUP
init_db()

app.include_router(business_router)
app.include_router(message_router)
app.include_router(auth_router)
app.include_router(webhook_router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal Server Error",
            "detail": str(exc)
        }
    )

@app.get("/")
def read_root():
    return {"message": "WhatsApp SAAS api running"}