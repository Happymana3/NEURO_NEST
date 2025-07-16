#!/usr/bin/env python3
"""
Quick start script for NeuroHub AI Assistant
"""
import subprocess
import sys
import os

def run_backend():
    """Start the FastAPI backend"""
    print("🚀 Starting NeuroHub Backend...")
    subprocess.run(["uv", "run", "uvicorn", "backend.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

def run_frontend():
    """Start the Streamlit frontend"""
    print("🎨 Starting NeuroHub Frontend...")
    subprocess.run(["uv", "run", "streamlit", "run", "frontend/app.py", "--server.port", "8501"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "backend":
            run_backend()
        elif sys.argv[1] == "frontend":
            run_frontend()
        else:
            print("Usage: python run.py [backend|frontend]")
    else:
        print("NeuroHub AI Assistant")
        print("Usage:")
        print("  uv run python run.py backend   # Start API server")
        print("  uv run python run.py frontend  # Start web interface")
        print("  docker-compose up              # Start both with Docker")