from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.library.helpers import openfile
from app.routers import accordion, twoforms, unsplash

app = FastAPI()


templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Return html for home page."""
    file_data = openfile("home.md")
    return templates.TemplateResponse(
        "page.html",
        {"request": request, "data": file_data},
    )


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def show_page(request: Request, page_name: str):
    """Return html for page identified by  page_name."""
    file_data = openfile("{0}.md".format(page_name))
    return templates.TemplateResponse(
        "page.html",
        {"request": request, "data": file_data},
    )
