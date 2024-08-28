from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./App/templates")
app.mount("/templates", StaticFiles(directory="./App/templates"), name="template")

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/add")
async def add(request: Request, name: str = Form(...), age: int = Form(...), grade: int = Form(...)):
    print(name)
    print(age)
    print(grade)
    return RedirectResponse(url=app.url_path_for("home_page"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/addnew", response_class=HTMLResponse)
async def addnew(request: Request):
    return templates.TemplateResponse(request=request, name="addnew.html")

@app.get("/students/id/{student_id}")
async def get_id(student_id: int):
    return {"id": student_id}