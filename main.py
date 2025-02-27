from fastapi import FastAPI
from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app  = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to ["http://localhost:5173"] for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message: Testing karaoke-app!"}

SONGS_FOLDER = Path("songs")
@app.get("/songs")
async def get_songs():
    if not SONGS_FOLDER.exists:
        return {"message": "The songs folder does not exist!"}
    
    songs = [file.stem for file in SONGS_FOLDER.glob("*") if file.suffix in (".mp4", ".mpeg", ".txt")]
    return JSONResponse(content={"songs": songs})

    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port="8000")