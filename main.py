from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Hello Recruto")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def hello_recruto(request: Request, name: str = 'Recruto', message: str = 'Давай дружить'):
    response = templates.TemplateResponse("index.html", {"request": request, "name": name, "message": message})
    return response
