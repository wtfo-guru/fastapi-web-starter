import os
from typing import Annotated

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from loguru import logger

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/twoforms", response_class=HTMLResponse)
def form_get(request: Request):
    """Handle get for two forms page.

    Parameters
    ----------
    request : Request
        The request to process

    Returns
    -------
    html : TemplateResponse
    """
    key = os.getenv("unsplash_key")
    logger.info(key)
    number = "Type a number"
    return templates.TemplateResponse(
        "twoforms.html",
        context={"request": request, "result": number},
    )


@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, number: Annotated[int, Form()]):
    """Return form1 post result.

    Parameters
    ----------
    request : Request
        The request to process
    number : int
        The number from the form

    Returns
    -------
    html : TemplateResponse
    """
    plus2 = number + 2
    return templates.TemplateResponse(
        "twoforms.html",
        context={"request": request, "result": plus2, "yournum": number},
    )


@router.post("/form2", response_class=HTMLResponse)
def form_post2(request: Request, number: Annotated[int, Form()]):
    """Return form2 post result.

    Parameters
    ----------
    request : Request
        The request to process
    number : int
        The number from the form

    Returns
    -------
    html : TemplateResponse
    """
    plus100 = number + 100
    return templates.TemplateResponse(
        "twoforms.html",
        context={"request": request, "result": plus100, "yournum": number},
    )
