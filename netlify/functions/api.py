import os
import sys

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from mangum import Mangum
from app.main import app

# This handler will be used by Netlify Functions
handler = Mangum(app, lifespan="off")
