import os

import markdown


def openfile(filename: str) -> dict[str, str]:
    """Return dictionary with key text equal to html for page."""
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text, extensions=['fenced_code'])
    return {"text": html}
