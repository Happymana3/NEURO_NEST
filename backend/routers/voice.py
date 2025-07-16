from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from backend.models.database import get_db, JournalEntry
from voice.recorder import VoiceProcessor
from mindmap.generator import MindMapGenerator

router = APIRouter()
voice_processor = VoiceProcessor()
mindmap_gen = MindMapGenerator()

@router.post("/transcribe")
async def transcribe_voice(audio: UploadFile = File(...), db: Session = Depends(get_db)):
    """Transcribe voice to text and create mind map"""
    audio_content = await audio.read()
    
    # Save audio temporarily
    with open(f"temp_{audio.filename}", "wb") as f:
        f.write(audio_content)
    
    # Transcribe
    text = voice_processor.transcribe_audio(f"temp_{audio.filename}")
    
    # Extract topics
    topics = voice_processor.extract_topics(text)
    
    # Generate mind map
    mindmap_html = mindmap_gen.create_mindmap(topics)
    
    # Save to database
    entry = JournalEntry(content=text, mood_score=0.5)
    db.add(entry)
    db.commit()
    
    return {
        "transcription": text,
        "topics": topics,
        "mindmap": mindmap_html
    }