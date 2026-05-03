from fastapi import FastAPI
from app.api.business import router as business_router

app = FastAPI()
app.include_router(business_router)

# Debug: print all registered routes
for route in app.routes:
    print(f"Route: {route.path} | Methods: {getattr(route, 'methods', None)}")

@app.get("/")
def read_root():
    return {"message": "WhatsApp SAAS api running"}