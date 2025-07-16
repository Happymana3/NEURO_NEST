#  NeuroHub AI Assistant

An AI-powered assistant supporting neurodivergent users (Dyslexia, ADHD, etc.) through multimodal interaction using Gemma 3n as the foundation model.

##  Features

###  Voice Journaling → Mind Maps
- Voice-to-text transcription using Whisper
- Automatic topic extraction
- Interactive mind map generation
- Mood detection and tracking

### Focus-Friendly Planner
- Natural language task parsing
- Smart scheduling with datetime extraction
- SQLite storage for persistence
- Simple task management

### Emotional Coach
- Emotion detection from text
- Personalized coping suggestions
- Mood history tracking
- Mental health support

###  AR Reading Assist
- OCR text extraction from images
- Text simplification for readability
- Text-to-speech conversion
- Dyslexia-friendly processing

### Language Learning (Planned)
- Flashcard system with spaced repetition
- Gamified learning experiences
- Adaptive difficulty

##  Tech Stack

**Backend:**
- FastAPI for REST API
- SQLAlchemy + SQLite for data persistence
- Whisper for speech-to-text
- OpenCV + Tesseract for OCR
- gTTS for text-to-speech

**Frontend:**
- Streamlit for MVP interface
- Pyvis for interactive mind maps

**Infrastructure:**
- Docker + Docker Compose
- Python 3.9

##  Quick Start

### Prerequisites
- Python 3.9+
- uv (recommended) or pip
- Docker (optional)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd gemma3n
```

2. **Install dependencies:**
```bash
uv sync
```

3. **Run the backend:**
```bash
uv run uvicorn backend.main:app --reload
```

4. **Run the frontend (in another terminal):**
```bash
uv run streamlit run frontend/app.py
```

### Using Docker

```bash
docker-compose up --build
```

- Backend API: http://localhost:8000
- Frontend UI: http://localhost:8501
- API Documentation: http://localhost:8000/docs

##  Project Structure

```
neurohub/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── routers/             # API endpoints
│   │   ├── voice.py         # Voice journaling
│   │   ├── planner.py       # Task planning
│   │   ├── coach.py         # Emotional coaching
│   │   ├── ar_reader.py     # OCR & TTS
│   │   └── mindmap.py       # Mind map generation
│   └── models/
│       └── database.py      # SQLAlchemy models
├── voice/
│   └── recorder.py          # Voice processing
├── planner/
│   └── parser.py            # Natural language parsing
├── coach/
│   └── emotion_model.py     # Emotion detection
├── mindmap/
│   └── generator.py         # Mind map creation
├── ar_reader/
│   └── ocr_reader.py        # OCR & text processing
├── lang_learning/
│   └── games/
│       └── flashcards.py    # Spaced repetition
├── frontend/
│   └── app.py               # Streamlit interface
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🔧 API Endpoints

### Voice Journaling
- `POST /voice/transcribe` - Upload audio for transcription and mind mapping

### Task Planning
- `POST /planner/add-task` - Add task from natural language
- `GET /planner/tasks` - Get all tasks

### Emotional Coaching
- `POST /coach/analyze-emotion` - Analyze emotion and get suggestions
- `GET /coach/mood-history` - Get mood tracking history

### AR Reading
- `POST /ar/read-image` - Extract and simplify text from image
- `POST /ar/text-to-speech` - Convert text to speech

### Mind Maps
- `POST /mindmap/generate` - Generate interactive mind map

##  Usage Examples

### Voice Journaling
1. Upload an audio file through the frontend
2. Get transcription and automatic mind map
3. View extracted topics and relationships

### Task Planning
```
Input: "remind me to do math homework at 3pm tomorrow"
Output: Structured task with parsed datetime
```

### Emotional Coaching
```
Input: "I'm feeling really anxious about my presentation"
Output: Emotion detection + coping suggestions
```

##  Future Enhancements

- Integration with Gemma 3n for advanced NLP
- React frontend with better UX
- Mobile app development
- Calendar synchronization
- Advanced AR features
- Multi-language support
- Voice-controlled interface

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

##  License

This project is licensed under the MIT License.
