from mangum import Mangum
from app.main import app

# This handler will be used by Netlify Functions
handler = Mangum(app, lifespan="off")
