from jinja2 import Environment, FileSystemLoader
from app.mock_data import BOOKS
import os

def verify_background():
    env = Environment(loader=FileSystemLoader("app/templates"))
    tmpl = env.get_template("book_reader.html")
    
    # Check book 1 (Cosmic Origins)
    book1 = next(b for b in BOOKS if b["id"] == 1)
    output1 = tmpl.render(book=book1, title=book1["title"])
    
    if "/static/images/cosmic_bg.jpg" in output1 and "book-reader-container" in output1:
        print("[PASS] Cosmic Origins has the background image referenced.")
    else:
        print("[FAIL] Cosmic Origins is missing the background image reference.")
        
    # Check book 2 (other)
    book2 = next(b for b in BOOKS if b["id"] == 2)
    output2 = tmpl.render(book=book2, title=book2["title"])
    
    if "/static/images/cosmic_bg.jpg" not in output2:
        print("[PASS] Other books do not have the cosmic background image.")
    else:
        print("[FAIL] Other books incorrectly show the cosmic background image.")

if __name__ == "__main__":
    verify_background()
