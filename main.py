# note does not run in jupyter notebook, run in terminal
from fastapi import FastAPI
import uvicorn
from src.get_text_data import get_wiki, get_random_wiki_page

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Template ML API to work with text data"}


@app.get("/wiki_summary/{page_name}")
async def wiki_summary(page_name: str):
    """Get the summary of a Wikipedia page"""

    result = get_wiki(page_name)
    return {"summary": result}


@app.get("/random_wiki_page")
async def random_wiki_page():
    """Get a random Wikipedia page summary"""

    result = get_wiki(get_random_wiki_page()[0])
    return {"summary": result}


if __name__ == "__main__":
    # goto localhost:8080/
    # or localhost:8080/docs for the interactive docs
    uvicorn.run(app, port=8080, host="0.0.0.0")
