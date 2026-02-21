from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from app.mock_data import BOOKS

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/books")
async def read_books(request: Request):
    return templates.TemplateResponse("books.html", {"request": request, "title": "Library", "books": BOOKS})

@router.get("/books/{book_id}")
async def read_book(request: Request, book_id: int):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return templates.TemplateResponse("book_reader.html", {"request": request, "title": book["title"], "book": book})
