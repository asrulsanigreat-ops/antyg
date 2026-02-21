from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="", tags=["auth"])

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Render the login page"""
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="app/templates")
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})

@router.get("/logout")
async def logout():
    """Logout route - client-side handles Firebase logout"""
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="app/templates")
    # Redirect to home after client-side logout
    return {"message": "Logged out successfully", "redirect": "/"}
