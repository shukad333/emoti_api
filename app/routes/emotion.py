from fastapi import APIRouter, UploadFile, File, HTTPException
from deepface import DeepFace
from PIL import Image
import io
import os
import numpy as np  # Import NumPy


router = APIRouter()


@router.post("/analyze/")
async def analyze_emotion(file: UploadFile = File(...)):
    try:
        # Read image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Save temporarily for DeepFace processing
        temp_path = "temp_image.jpg"
        image.save(temp_path)

        # Analyze emotions with enforce_detection=False
        analysis = DeepFace.analyze(temp_path, actions=['emotion'], enforce_detection=False)
        os.remove(temp_path)  # Clean up temp file

        # Convert NumPy float32 values to Python float
        emotions = {k: float(v) for k, v in analysis[0]["emotion"].items()}

        return {"emotions": emotions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

