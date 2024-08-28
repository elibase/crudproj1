from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./App/templates")
app.mount("/templates", StaticFiles(directory="./App/templates"), name="template")

#read
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/addnew", response_class=HTMLResponse)
async def addnew(request: Request):
    return templates.TemplateResponse(request=request, name="addnew.html")

@app.get("/students/id/{student_id}")
async def get_id(student_id: int):
    return {"id": student_id}