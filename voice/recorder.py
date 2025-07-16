import whisper
import io
from typing import Dict

class VoiceProcessor:
    def __init__(self):
        self.model = whisper.load_model("base")
    
    def transcribe_audio(self, audio_file) -> str:
        """Transcribe audio file to text"""
        result = self.model.transcribe(audio_file)
        return result["text"]
    
    def extract_topics(self, text: str) -> Dict:
        """Extract main topics and subtopics from text"""
        # Simple keyword extraction - can be enhanced with Gemma 3n
        sentences = text.split('.')
        topics = {}
        
        for i, sentence in enumerate(sentences):
            if sentence.strip():
                topic_key = f"topic_{i+1}"
                topics[topic_key] = {
                    "main": sentence.strip()[:50],
                    "full": sentence.strip()
                }
        
        return topics