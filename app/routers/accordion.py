from typing import Annotated

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/accordion", response_class=HTMLResponse)
def get_accordion(request: Request):
    """Handle get for accordion page.

    Parameters
    ----------
    request : Request
        The request to process

    Returns
    -------
    html : TemplateResponse
    """
    tag = "flower"
    caption = "Type a number"
    return templates.TemplateResponse(
        "accordion.html",
        context={"request": request, "result": caption, "tag": tag},
    )


@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: Annotated[str, Form()]):
    """Handle post for accordion page.

    Parameters
    ----------
    request : Request
        The request to process
    tag : str
        The tag from the page

    Returns
    -------
    html : TemplateResponse
    """
    return templates.TemplateResponse(
        "accordion.html",
        context={"request": request, "tag": tag},
    )
