from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.scraper import parse_website
from app.utils import check_parsable
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def parse_url(request: Request, url: str = Form(...)):
    error_message = None  
    if check_parsable(url):
        data = parse_website(url)
        return templates.TemplateResponse("result.html", {"request": request, "data": data})
    else:
        error_message = "Сайт нельзя парсить или он недоступен." 
        return templates.TemplateResponse("index.html", {"request": request, "error_message": error_message})

