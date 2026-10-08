"""Exercise starter: the server works, but GET /tides is not implemented yet.

    uv run pywrangler dev week04/tdd_api.py

Add the route below, using the existing data loader and selection rule.
"""

from fastapi import FastAPI, Query

try:
    from workers import asgi
except ImportError:  # Local FastAPI runs do not install the Cloudflare adapter.
    asgi = None

try:
    from .api import load_rows
    from .transform import select_month
except ImportError:  # The Worker loads this file as a top-level module.
    from api import load_rows
    from transform import select_month

app = FastAPI(title="Week 4 · test first")


@app.get("/tides")
def tides(month: int = Query(ge=1, le=12)):
    """Return one month's daily records as JSON."""
    return select_month(load_rows(), month)


Default = asgi.entrypoint(app) if asgi is not None else app
