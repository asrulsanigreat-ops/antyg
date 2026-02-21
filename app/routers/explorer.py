from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.mock_data import CHEMISTRY

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/chemistry", response_class=HTMLResponse)
async def read_chemistry(request: Request):
    return templates.TemplateResponse("explorer.html", {"request": request, "title": "Eksplorasi Kimia", "chemistry": CHEMISTRY})

@router.get("/chemistry/{article_id}", response_class=HTMLResponse)
async def read_chemistry_article(request: Request, article_id: int):
    """Display individual chemistry article"""
    article = next((a for a in CHEMISTRY if a["id"] == article_id), None)
    if not article:
        raise HTTPException(status_code=404, detail="Chemistry article not found")
    
    return templates.TemplateResponse("explorer_article.html", {
        "request": request,
        "title": article["title"],
        "article": article
    })
