from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import voice, planner, coach, mindmap, ar_reader
from backend.models.database import init_db

app = FastAPI(title="NeuroHub AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice.router, prefix="/voice", tags=["voice"])
app.include_router(planner.router, prefix="/planner", tags=["planner"])
app.include_router(coach.router, prefix="/coach", tags=["coach"])
app.include_router(mindmap.router, prefix="/mindmap", tags=["mindmap"])
app.include_router(ar_reader.router, prefix="/ar", tags=["ar"])

@app.on_event("startup")
async def startup():
    init_db()

@app.get("/")
async def root():
    return {"message": "NeuroHub AI Assistant API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)