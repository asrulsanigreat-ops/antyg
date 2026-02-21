from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.mock_data import JOURNALS

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/journals", response_class=HTMLResponse)
async def read_journals(request: Request):
    """Display all journal articles"""
    return templates.TemplateResponse("journals.html", {
        "request": request,
        "title": "Science Journals",
        "journals": JOURNALS
    })

@router.get("/journals/{journal_id}", response_class=HTMLResponse)
async def read_journal_article(request: Request, journal_id: int):
    """Display individual journal article with Wikipedia-style layout"""
    journal = next((j for j in JOURNALS if j["id"] == journal_id), None)
    if not journal:
        raise HTTPException(status_code=404, detail="Journal article not found")
    
    return templates.TemplateResponse("journal_article.html", {
        "request": request,
        "title": journal["title"],
        "journal": journal
    })

