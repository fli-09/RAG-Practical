from fastapi import FastAPI, Form, Request, File
from fastapi.responses import RedirectResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import aiofiles
import csv
import io
from src.helper import llm_pipeline

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def chat(request: Request, pdf_file: bytes = File(), filename: str = Form(...)):
    base_folder = 'static/docs'
    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)
    pdf_filename = os.path.join(base_folder, filename)

    async with aiofiles.open(pdf_filename, "wb") as f:
        await f.write(pdf_file)

    # Extract questions only
    ques_list = llm_pipeline(pdf_filename)

    # Write questions to in-memory CSV
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Question"])
    for question in ques_list:
        writer.writerow([question])
    output.seek(0)

    # Return as downloadable file
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=questions_{filename}.csv"
        }
    )

if __name__ == "__main__":
    uvicorn.run("app:app",host = '0.0.0.0',port = 8000,reload =True)    