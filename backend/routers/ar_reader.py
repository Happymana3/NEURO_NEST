from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from ar_reader.ocr_reader import OCRReader
import io

router = APIRouter()
ocr_reader = OCRReader()

@router.post("/read-image")
async def read_image(image: UploadFile = File(...)):
    """Extract and simplify text from image"""
    # Save uploaded image
    image_path = f"temp_{image.filename}"
    with open(image_path, "wb") as f:
        content = await image.read()
        f.write(content)
    
    # Extract text
    text = ocr_reader.extract_text(image_path)
    simplified_text = ocr_reader.simplify_text(text)
    
    return {
        "original_text": text,
        "simplified_text": simplified_text
    }

@router.post("/text-to-speech")
async def text_to_speech(text: str):
    """Convert text to speech audio"""
    audio_data = ocr_reader.text_to_speech(text)
    
    return StreamingResponse(
        io.BytesIO(audio_data),
        media_type="audio/mpeg",
        headers={"Content-Disposition": "attachment; filename=speech.mp3"}
    )