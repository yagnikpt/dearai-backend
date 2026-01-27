from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.chat.router import router as chat_router
from app.config import settings
from app.conversations.router import router as conversations_router
from app.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown


app = FastAPI(
    title=settings.app_name,
    description="Mental health companion chat API with voice support",
    version="0.1.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(conversations_router, prefix="/conversations", tags=["Conversations"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
