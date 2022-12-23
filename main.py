# note does not run in jupyter notebook, run in terminal
from fastapi import FastAPI
import uvicorn
from src.input_data import get_wiki_page, get_random_wiki_page
from src.control import Job_list

app = FastAPI()

# create the job list
jobs = Job_list()


# OUTPUT
@app.get("/")
async def root():
    return {"message": "Template ML API to work with text data"}


@app.get("/wiki_page/{page_name}")
async def wiki_page(page_name: str):
    """Get the text content of a Wikipedia page"""

    result = get_wiki_page(page_name)
    return {"title": page_name, "content": result}


@app.get("/random_wiki_page")
async def random_wiki_page():
    """Get a random Wikipedia page summary"""
    page_title = get_random_wiki_page()[0]
    result = get_wiki_page(page_title)
    return {"title": page_title, "content": result}


@app.get("/get_current_jobs")
async def get_current_jobs():
    """Get the current jobs"""
    return {"jobs": jobs.jobs}


# INPUT
@app.post("/add_job/{job}")
async def add_job(job: str):
    """Add a job to the list of jobs"""
    jobs.add(job)
    return {"message": "Job added"}


@app.post("/remove_job/{job}")
async def remove_job(job: str):
    """Remove a job from the list of jobs"""
    jobs.remove(job)
    return {"message": "Job removed"}


if __name__ == "__main__":
    # goto localhost:8080/
    # or localhost:8080/docs for the interactive docs
    uvicorn.run(app, port=8080, host="0.0.0.0")
