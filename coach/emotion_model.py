import re
from typing import Dict

class EmotionDetector:
    def __init__(self):
        self.emotion_keywords = {
            'happy': ['happy', 'joy', 'excited', 'great', 'awesome', 'wonderful'],
            'sad': ['sad', 'down', 'depressed', 'upset', 'crying'],
            'angry': ['angry', 'mad', 'furious', 'annoyed', 'frustrated'],
            'anxious': ['anxious', 'worried', 'nervous', 'stressed', 'panic'],
            'calm': ['calm', 'peaceful', 'relaxed', 'serene', 'tranquil']
        }
    
    def detect_emotion(self, text: str) -> Dict:
        """Simple emotion detection from text"""
        text_lower = text.lower()
        emotion_scores = {}
        
        for emotion, keywords in self.emotion_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            emotion_scores[emotion] = score
        
        # Get dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        confidence = emotion_scores[dominant_emotion] / len(text.split()) if text.split() else 0
        
        return {
            'emotion': dominant_emotion,
            'confidence': confidence,
            'scores': emotion_scores
        }
    
    def get_suggestion(self, emotion: str) -> str:
        """Get coping suggestion based on emotion"""
        suggestions = {
            'anxious': "Try deep breathing: inhale for 4, hold for 4, exhale for 4",
            'sad': "Consider journaling your thoughts or talking to someone you trust",
            'angry': "Take a 5-minute break and try progressive muscle relaxation",
            'happy': "Great! Consider sharing this positive moment in your journal",
            'calm': "Perfect state for reflection or planning your day"
        }
        return suggestions.get(emotion, "Take a moment to check in with yourself")