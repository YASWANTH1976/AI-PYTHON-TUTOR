import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

TEACHING_STYLES = {
    "visual": "🎨 ASCII diagrams, flowcharts, visualizations",
    "verbal": "📚 Detailed explanations, analogies",
    "kinesthetic": "🎮 Hands-on, exercises, experiments",
    "socratic": "❓ Guiding questions, discovery"
}

PYTHON_TOPICS = [
    "Basics",
    "Operators",
    "Control Flow",
    "Loops",
    "Data Structures",
    "Functions",
    "Advanced",
    "OOP",
    "Strings",
    "Files",
    "Errors",
    "Modules",
    "Best Practices"
]

MAX_EXECUTION_TIMEOUT = 5
ENABLE_VOICE_INPUT = True
ENABLE_VISUAL_SUMMARIES = True