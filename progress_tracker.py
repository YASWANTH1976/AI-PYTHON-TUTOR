import json
import os
from datetime import datetime
from typing import Dict, List

LEVELS = {
    1: {"name": "Beginner", "xp_required": 0, "color": "#90EE90"},
    2: {"name": "Novice", "xp_required": 100, "color": "#87CEEB"},
    3: {"name": "Intermediate", "xp_required": 300, "color": "#FFD700"},
    4: {"name": "Advanced", "xp_required": 600, "color": "#FF6347"},
    5: {"name": "Expert", "xp_required": 1000, "color": "#9370DB"},
    6: {"name": "Master", "xp_required": 1500, "color": "#FF1493"}
}

XP_REWARDS = {
    "lesson_complete": 20,
    "exercise_correct": 15,
    "code_explain": 10,
    "code_review": 15,
    "hint_request": 5,
    "message": 5
}

class ProgressTracker:
    def __init__(self, username: str = "student"):
        self.username = username
        self.progress_file = f"progress_{username}.json"
        self.data = self.load_progress()
    
    def load_progress(self) -> Dict:
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        else:
            return {
                "username": self.username,
                "xp": 0,
                "level": 1,
                "completed_lessons": [],
                "completed_exercises": [],
                "current_streak": 0,
                "last_activity": None,
                "achievements": [],
                "teaching_style": "visual"
            }
    
    def save_progress(self):
        with open(self.progress_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_xp(self, xp: int, reason: str = ""):
        old_level = self.data["level"]
        self.data["xp"] += xp
        
        new_level = self.calculate_level()
        if new_level > old_level:
            self.data["level"] = new_level
            self.data["achievements"].append(f"🎉 Reached Level {new_level}!")
        
        self.data["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_progress()
        return new_level > old_level
    
    def calculate_level(self) -> int:
        for level in sorted(LEVELS.keys(), reverse=True):
            if self.data["xp"] >= LEVELS[level]["xp_required"]:
                return level
        return 1
    
    def get_stats(self) -> Dict:
        return {
            "level": self.data["level"],
            "level_name": LEVELS[self.data["level"]]["name"],
            "xp": self.data["xp"],
            "lessons_completed": len(self.data["completed_lessons"]),
            "exercises_completed": len(self.data["completed_exercises"]),
            "current_streak": self.data["current_streak"],
            "achievements": self.data["achievements"]
        }

progress = ProgressTracker()

def get_stats() -> Dict:
    return progress.get_stats()

def add_xp(xp: int, reason: str = ""):
    return progress.add_xp(xp, reason)