from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models.database import get_db, JournalEntry
from coach.emotion_model import EmotionDetector
from pydantic import BaseModel

router = APIRouter()
emotion_detector = EmotionDetector()

class EmotionRequest(BaseModel):
    text: str

@router.post("/analyze-emotion")
async def analyze_emotion(request: EmotionRequest, db: Session = Depends(get_db)):
    """Analyze emotion and provide coaching"""
    emotion_data = emotion_detector.detect_emotion(request.text)
    suggestion = emotion_detector.get_suggestion(emotion_data['emotion'])
    
    # Save to journal with mood score
    mood_score = emotion_data['confidence']
    entry = JournalEntry(content=request.text, mood_score=mood_score)
    db.add(entry)
    db.commit()
    
    return {
        'emotion': emotion_data,
        'suggestion': suggestion,
        'mood_score': mood_score
    }

@router.get("/mood-history")
async def get_mood_history(db: Session = Depends(get_db)):
    """Get mood history for tracking"""
    entries = db.query(JournalEntry).order_by(JournalEntry.created_at.desc()).limit(10).all()
    return {"mood_history": [{"date": e.created_at, "score": e.mood_score} for e in entries]}