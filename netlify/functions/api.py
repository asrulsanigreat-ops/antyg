import os
import sys

# Netlify/Lambda environment check
lambda_root = os.environ.get("LAMBDA_TASK_ROOT")
if lambda_root:
    project_root = lambda_root
else:
    # Local/Fallback
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "../.."))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from mangum import Mangum

try:
    from app.main import app
except ImportError as e:
    # Log details for Netlify Functions logs
    print(f"DEBUG: project_root={project_root}")
    print(f"DEBUG: sys.path={sys.path}")
    print(f"DEBUG: os.getcwd()={os.getcwd()}")
    raise e

# Create the Mangum handler
handler = Mangum(app, lifespan="off")
