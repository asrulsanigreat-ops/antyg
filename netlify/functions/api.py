import os
import sys

# Get the directory of the current file (netlify/functions/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# The project root is two levels up
project_root = os.path.abspath(os.path.join(current_dir, "../.."))

# Add the project root to sys.path to allow imports from the 'app' module
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from mangum import Mangum

try:
    from app.main import app
except ImportError as e:
    print(f"ImportError: {e}")
    print(f"sys.path: {sys.path}")
    print(f"Current directory: {os.getcwd()}")
    raise

# Create the Mangum handler
handler = Mangum(app, lifespan="off")
