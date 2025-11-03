
# 🚀 COMPREHENSIVE PYTHON CURRICULUM (62 TOPICS)

LESSONS = {
    "1": {"title": "🎯 Variables & Data Types", "topic": "basics", "difficulty": "Beginner", "duration": "15 mins"},
    "2": {"title": "🔢 Numbers (int, float, complex)", "topic": "basics", "difficulty": "Beginner", "duration": "15 mins"},
    "3": {"title": "📝 Strings & Text Processing", "topic": "basics", "difficulty": "Beginner", "duration": "20 mins"},
    "4": {"title": "✅ Booleans & Logic", "topic": "basics", "difficulty": "Beginner", "duration": "10 mins"},
    "5": {"title": "➕ Arithmetic Operators", "topic": "operators", "difficulty": "Beginner", "duration": "15 mins"},
    "6": {"title": "🔗 Comparison Operators", "topic": "operators", "difficulty": "Beginner", "duration": "15 mins"},
    "7": {"title": "🧠 Logical Operators (and, or, not)", "topic": "operators", "difficulty": "Beginner", "duration": "15 mins"},
    "8": {"title": "🔄 Assignment & Compound Operators", "topic": "operators", "difficulty": "Beginner", "duration": "10 mins"},
    "9": {"title": "🎭 Bitwise Operators", "topic": "operators", "difficulty": "Intermediate", "duration": "20 mins"},
    "10": {"title": "🔀 If/Elif/Else Statements", "topic": "control", "difficulty": "Beginner", "duration": "20 mins"},
    "11": {"title": "🎯 Ternary Operator", "topic": "control", "difficulty": "Beginner", "duration": "10 mins"},
    "12": {"title": "🚦 Switch-like with dict", "topic": "control", "difficulty": "Intermediate", "duration": "15 mins"},
    "13": {"title": "🔁 For Loops", "topic": "loops", "difficulty": "Beginner", "duration": "20 mins"},
    "14": {"title": "⚙️ While Loops", "topic": "loops", "difficulty": "Beginner", "duration": "20 mins"},
    "15": {"title": "🔂 Nested Loops", "topic": "loops", "difficulty": "Intermediate", "duration": "20 mins"},
    "16": {"title": "🛑 Break & Continue", "topic": "loops", "difficulty": "Beginner", "duration": "15 mins"},
    "17": {"title": "⚡ Loop Else Clause", "topic": "loops", "difficulty": "Intermediate", "duration": "15 mins"},
    "18": {"title": "📋 Lists & Indexing", "topic": "data_structures", "difficulty": "Beginner", "duration": "20 mins"},
    "19": {"title": "🔒 Tuples & Unpacking", "topic": "data_structures", "difficulty": "Beginner", "duration": "20 mins"},
    "20": {"title": "🗂️ Dictionaries", "topic": "data_structures", "difficulty": "Beginner", "duration": "25 mins"},
    "21": {"title": "🎯 Sets & Operations", "topic": "data_structures", "difficulty": "Intermediate", "duration": "20 mins"},
    "22": {"title": "✨ List Comprehensions", "topic": "data_structures", "difficulty": "Intermediate", "duration": "20 mins"},
    "23": {"title": "🎁 Dict Comprehensions", "topic": "data_structures", "difficulty": "Intermediate", "duration": "15 mins"},
    "24": {"title": "💫 Set Comprehensions", "topic": "data_structures", "difficulty": "Intermediate", "duration": "15 mins"},
    "25": {"title": "🔗 Slicing & Indexing", "topic": "data_structures", "difficulty": "Intermediate", "duration": "20 mins"},
    "26": {"title": "🔧 Defining & Calling Functions", "topic": "functions", "difficulty": "Beginner", "duration": "20 mins"},
    "27": {"title": "📤 Return Values & Multiple Returns", "topic": "functions", "difficulty": "Beginner", "duration": "15 mins"},
    "28": {"title": "🎯 Arguments & Parameters", "topic": "functions", "difficulty": "Intermediate", "duration": "20 mins"},
    "29": {"title": "⭐ *args & **kwargs", "topic": "functions", "difficulty": "Intermediate", "duration": "25 mins"},
    "30": {"title": "📌 Default Arguments", "topic": "functions", "difficulty": "Intermediate", "duration": "15 mins"},
    "31": {"title": "🔄 Recursion & Base Cases", "topic": "functions", "difficulty": "Intermediate", "duration": "25 mins"},
    "32": {"title": "📍 Scope & LEGB Rule", "topic": "functions", "difficulty": "Intermediate", "duration": "20 mins"},
    "33": {"title": "🎭 Lambda Functions", "topic": "functions", "difficulty": "Intermediate", "duration": "15 mins"},
    "34": {"title": "🎨 Decorators Basics", "topic": "advanced", "difficulty": "Advanced", "duration": "30 mins"},
    "35": {"title": "🌊 Generators & yield", "topic": "advanced", "difficulty": "Advanced", "duration": "30 mins"},
    "36": {"title": "🔍 Iterators & iter()", "topic": "advanced", "difficulty": "Advanced", "duration": "25 mins"},
    "37": {"title": "📚 Context Managers (with)", "topic": "advanced", "difficulty": "Advanced", "duration": "25 mins"},
    "38": {"title": "🗺️ Map, Filter, Reduce", "topic": "advanced", "difficulty": "Advanced", "duration": "20 mins"},
    "39": {"title": "🏗️ Classes & Objects", "topic": "oop", "difficulty": "Intermediate", "duration": "25 mins"},
    "40": {"title": "🎯 Methods & self", "topic": "oop", "difficulty": "Intermediate", "duration": "20 mins"},
    "41": {"title": "🔐 __init__ Constructor", "topic": "oop", "difficulty": "Intermediate", "duration": "20 mins"},
    "42": {"title": "🧬 Inheritance", "topic": "oop", "difficulty": "Advanced", "duration": "30 mins"},
    "43": {"title": "🎭 Polymorphism", "topic": "oop", "difficulty": "Advanced", "duration": "25 mins"},
    "44": {"title": "🔒 Encapsulation & Properties", "topic": "oop", "difficulty": "Advanced", "duration": "25 mins"},
    "45": {"title": "🌟 Magic Methods (__str__, __repr__)", "topic": "oop", "difficulty": "Advanced", "duration": "20 mins"},
    "46": {"title": "👥 Class & Static Methods", "topic": "oop", "difficulty": "Advanced", "duration": "20 mins"},
    "47": {"title": "🔤 String Methods & Formatting", "topic": "strings", "difficulty": "Beginner", "duration": "20 mins"},
    "48": {"title": "🎨 f-strings & Interpolation", "topic": "strings", "difficulty": "Beginner", "duration": "15 mins"},
    "49": {"title": "🔍 Regular Expressions (Regex)", "topic": "strings", "difficulty": "Advanced", "duration": "40 mins"},
    "50": {"title": "📁 File Reading & Writing", "topic": "files", "difficulty": "Intermediate", "duration": "20 mins"},
    "51": {"title": "📊 Working with JSON", "topic": "files", "difficulty": "Intermediate", "duration": "20 mins"},
    "52": {"title": "🗃️ CSV & Data Files", "topic": "files", "difficulty": "Intermediate", "duration": "20 mins"},
    "53": {"title": "🚨 Try/Except/Finally", "topic": "errors", "difficulty": "Intermediate", "duration": "25 mins"},
    "54": {"title": "⚠️ Raising Custom Exceptions", "topic": "errors", "difficulty": "Intermediate", "duration": "20 mins"},
    "55": {"title": "🛡️ Exception Hierarchy", "topic": "errors", "difficulty": "Advanced", "duration": "20 mins"},
    "56": {"title": "📦 Importing Modules", "topic": "modules", "difficulty": "Beginner", "duration": "15 mins"},
    "57": {"title": "📚 Python Standard Library", "topic": "modules", "difficulty": "Intermediate", "duration": "30 mins"},
    "58": {"title": "🔧 Virtual Environments & pip", "topic": "modules", "difficulty": "Intermediate", "duration": "20 mins"},
    "59": {"title": "✨ PEP 8 & Code Style", "topic": "best_practices", "difficulty": "Intermediate", "duration": "20 mins"},
    "60": {"title": "🧪 Unit Testing with unittest", "topic": "best_practices", "difficulty": "Advanced", "duration": "30 mins"},
    "61": {"title": "⚡ Performance & Optimization", "topic": "best_practices", "difficulty": "Advanced", "duration": "30 mins"},
    "62": {"title": "🐛 Debugging Techniques", "topic": "best_practices", "difficulty": "Intermediate", "duration": "25 mins"},
}

# ============================================================================
# HELPER FUNCTIONS - THESE ARE REQUIRED FOR IMPORTS
# ============================================================================

def get_lesson(lesson_id: str):
    """Get a specific lesson by ID"""
    return LESSONS.get(lesson_id, None)

def get_all_lessons():
    """Get list of all lessons (ID, title pairs)"""
    return [(key, lesson["title"]) for key, lesson in LESSONS.items()]

def get_lessons_by_topic(topic: str):
    """Get all lessons for a specific topic"""
    return [(key, lesson) for key, lesson in LESSONS.items() if lesson.get("topic") == topic]

def get_all_topics():
    """Get unique topics from all lessons"""
    return list(set(lesson.get("topic") for lesson in LESSONS.values()))

def get_topic_name(topic: str) -> str:
    """Get display name for a topic"""
    names = {
        "basics": "🎯 Python Basics",
        "operators": "➕ Operators & Expressions",
        "control": "🔀 Control Flow",
        "loops": "🔁 Loops",
        "data_structures": "📊 Data Structures",
        "functions": "🔧 Functions",
        "advanced": "🎨 Advanced Features",
        "oop": "🏗️ Object-Oriented Programming",
        "strings": "🔤 Strings & Text",
        "files": "📁 File Handling",
        "errors": "🚨 Error Handling",
        "modules": "📦 Modules & Packages",
        "best_practices": "✨ Best Practices"
    }
    return names.get(topic, topic)