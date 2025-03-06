from fastapi import FastAPI
#from app.routes.auth import router as auth_router
from app.routes.emotion import router as emotion_router
#from app.routes.trends import router as trends_router
#from app.database import init_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Emotion API is running!"}

# Include API routes
#app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(emotion_router, prefix="/emotion", tags=["Emotion Analysis"])
#app.include_router(trends_router, prefix="/trends", tags=["Trend Analysis"])

# Initialize Database
@app.on_event("startup")
def startup():
    #init_db()
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
