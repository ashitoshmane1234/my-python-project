from fastapi import FastAPI
from .users.routes import router as users_router
from .greetings.routes import router as greetings_router

app = FastAPI(title="Modular API with Users")

app.include_router(users_router)
app.include_router(greetings_router)