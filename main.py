from fastapi import FastAPI, Query

app = FastAPI(title = "Hello Recruto")


@app.get("/")
async def Hello_Recruto(
	name: str = Query('Recruto'),
	message: str = Query('Давай дружить')):
    return f"Hello {name}! {message}"
