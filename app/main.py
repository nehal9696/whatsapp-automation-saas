from fastapi import FastAPI
from app.api.business import router as business_router
from app.db.init_db import init_db
from app.api.message import router as message_router

app = FastAPI()

# CREATE TABLES ON STARTUP
init_db()

app.include_router(business_router)
app.include_router(message_router)


@app.get("/")
def read_root():
    return {"message": "WhatsApp SAAS api running"}