from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

app = FastAPI(
    title="Science Learning Platform",
    description="A futuristic platform for learning science.",
    version="0.1.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home"})

from app.routers import books, journals, quizzes, explorer, auth
app.include_router(books.router)
app.include_router(journals.router)
app.include_router(quizzes.router)
app.include_router(explorer.router)
app.include_router(auth.router)
