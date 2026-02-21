import sys
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("app/templates"))
try:
    tmpl = env.get_template("books.html")
    print("Template parsed successfully.")
except Exception as e:
    print(f"Template error: {e}")
