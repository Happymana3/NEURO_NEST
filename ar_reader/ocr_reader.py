import cv2
import pytesseract
from gtts import gTTS
import io
from typing import Dict

class OCRReader:
    def extract_text(self, image_path: str) -> str:
        """Extract text from image using OCR"""
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text.strip()
    
    def simplify_text(self, text: str) -> str:
        """Simplify text for better readability"""
        # Basic text simplification
        sentences = text.split('.')
        simplified = []
        
        for sentence in sentences:
            if len(sentence.strip()) > 10:  # Keep meaningful sentences
                # Remove complex punctuation
                clean = sentence.strip().replace(',', ' ')
                simplified.append(clean)
        
        return '. '.join(simplified)
    
    def text_to_speech(self, text: str) -> bytes:
        """Convert text to speech audio"""
        tts = gTTS(text=text, lang='en', slow=True)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer.getvalue()