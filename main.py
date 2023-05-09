import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers


app = FastAPI(
    contact=dict(
        email="geral@knowldgzebiz.pt",
        http="https://knowledgebiz.pt"
    ),
    version="1.0.0",
    title="API SINGULAR ROUTE",
    description="This API integrates with SINGULAR ROUTE system"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routers.user_router.router, prefix="/user", tags=["user"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2828)
