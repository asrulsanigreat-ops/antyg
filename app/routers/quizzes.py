from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.mock_data import QUIZZES
from typing import List
import json

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Store quiz sessions in memory (in production, use a database or session storage)
quiz_sessions = {}

@router.get("/tests", response_class=HTMLResponse)
async def read_quizzes(request: Request):
    """Display all available quizzes"""
    return templates.TemplateResponse("quizzes.html", {
        "request": request, 
        "title": "Knowledge Checks", 
        "quizzes": QUIZZES
    })

@router.get("/tests/{quiz_id}", response_class=HTMLResponse)
async def start_quiz(request: Request, quiz_id: int):
    """Start a quiz or display the quiz-taking interface"""
    quiz = next((q for q in QUIZZES if q["id"] == quiz_id), None)
    if not quiz:
        return RedirectResponse(url="/tests")
    
    return templates.TemplateResponse("quiz_taking.html", {
        "request": request,
        "title": f"Quiz: {quiz['title']}",
        "quiz": quiz
    })

@router.post("/tests/{quiz_id}/submit", response_class=HTMLResponse)
async def submit_quiz(request: Request, quiz_id: int):
    """Process quiz submission and show results"""
    quiz = next((q for q in QUIZZES if q["id"] == quiz_id), None)
    if not quiz:
        return RedirectResponse(url="/tests")
    
    # Get form data
    form_data = await request.form()
    
    # Calculate score
    correct_count = 0
    total_questions = len(quiz["questions"])
    total_points = 0
    max_points = sum(q["points"] for q in quiz["questions"])
    results = []
    
    for question in quiz["questions"]:
        q_id = str(question["id"])
        user_answer = form_data.get(f"question_{q_id}")
        
        # Handle true/false questions
        if question["type"] == "true_false":
            user_answer = user_answer == "True" if user_answer else None
            correct_answer = question["correct_answer"]
        else:
            correct_answer = question["correct_answer"]
        
        is_correct = str(user_answer) == str(correct_answer)
        
        if is_correct:
            correct_count += 1
            total_points += question["points"]
        
        results.append({
            "question": question["question"],
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "explanation": question["explanation"],
            "type": question["type"],
            "options": question.get("options", [])
        })
    
    # Calculate percentage and XP
    percentage = (correct_count / total_questions * 100) if total_questions > 0 else 0
    xp_earned = int(quiz["xp_reward"] * (percentage / 100))
    
    # Determine badge based on score
    if percentage >= 90:
        badge = "gold"
        badge_text = "🏆 Gold Medal"
    elif percentage >= 70:
        badge = "silver"
        badge_text = "🥈 Silver Medal"
    elif percentage >= 50:
        badge = "bronze"
        badge_text = "🥉 Bronze Medal"
    else:
        badge = "none"
        badge_text = "Keep Practicing!"
    
    return templates.TemplateResponse("quiz_results.html", {
        "request": request,
        "title": f"Results: {quiz['title']}",
        "quiz": quiz,
        "results": results,
        "correct_count": correct_count,
        "total_questions": total_questions,
        "percentage": round(percentage, 1),
        "total_points": total_points,
        "max_points": max_points,
        "xp_earned": xp_earned,
        "badge": badge,
        "badge_text": badge_text
    })

