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
app.include_router(routers.history_router.router, prefix="/history", tags=["history"])
app.include_router(routers.wishlist_router.router, prefix="/wishlist", tags=["wishlist"])
app.include_router(routers.restaurants_router.router, prefix="/restaurants", tags=["restaurants"])
app.include_router(routers.attraction_router.router, prefix="/attractions", tags=["attraction"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2828)
