from jinja2 import Environment, FileSystemLoader
from app.mock_data import BOOKS

env = Environment(loader=FileSystemLoader("app/templates"))
try:
    tmpl = env.get_template("books.html")
    # minimal mock request object
    class MockRequest:
        pass
    
    output = tmpl.render(request=MockRequest(), title="Library", books=BOOKS)
    print("Template rendered successfully.")
    # print(output[:500]) # print first 500 chars
except Exception as e:
    print(f"Template render error: {e}")
