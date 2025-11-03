import os
import importlib
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

def safe_import(module_name, item_name=None):
    try:
        module = importlib.import_module(module_name)
        if item_name:
            return getattr(module, item_name, None)
        return module
    except ImportError:
        return None

ChatGroq = safe_import("langchain_groq", "ChatGroq")
HumanMessage = safe_import("langchain_core.messages", "HumanMessage")
SystemMessage = safe_import("langchain_core.messages", "SystemMessage")

if HumanMessage is None:
    _lc_schema = safe_import("langchain.schema")
    if _lc_schema:
        HumanMessage = getattr(_lc_schema, "HumanMessage", None)
        SystemMessage = getattr(_lc_schema, "SystemMessage", None)

if HumanMessage is None:
    class HumanMessage:
        def __init__(self, content):
            self.content = content

if SystemMessage is None:
    class SystemMessage:
        def __init__(self, content):
            self.content = content

class PythonTutor:
    def __init__(self, teaching_style: str = "visual"):
        self.teaching_style = teaching_style
        self.conversation_history = []
        self.model = None
        self._init_error = None

    def _get_system_prompt(self) -> str:
        base = """You are WORLD'S #1 PYTHON TUTOR combining expertise of:
- Corey Schafer (crystal-clear explanations)
- David Beazley (deep technical knowledge)
- Raymond Hettinger (Pythonic best practices)
- Al Sweigart (practical real-world approach)
- Angela Yu (engaging project-based)

CORE PRINCIPLES:
1. ALWAYS analyze the EXACT code provided - be SPECIFIC not generic
2. Explain EVERY LINE of code with WHY it matters
3. Show INPUT → PROCESSING → OUTPUT flow
4. Compare with alternative approaches
5. Highlight edge cases and potential bugs
6. Provide ALWAYS runnable examples
7. Use visual diagrams and ASCII art where helpful

CAN ANSWER ANY PYTHON TOPIC:
- Basics to Advanced
- OOP, Functional Programming
- Frameworks (Django, Flask)
- Libraries (NumPy, Pandas, etc)
- Performance & Optimization
- Debugging & Testing
- System Design

TEACHING STYLE: """ + self._get_style_prompt()
        return base

    def _get_style_prompt(self) -> str:
        styles = {
            "visual": "🎨 ASCII flowcharts, step-by-step diagrams, before/after comparisons, memory visualization",
            "verbal": "📚 Detailed explanations, multiple analogies, rich vocabulary, extended examples",
            "kinesthetic": "🎮 More exercises, encourage experimentation, interactive snippets, learning by doing",
            "socratic": "❓ Ask guiding questions, help discover answers, hints not solutions, build critical thinking"
        }
        return styles.get(self.teaching_style, styles["visual"])

    def _init_model(self):
        if self.model is not None:
            return
        if ChatGroq is None:
            self._init_error = "Install: pip install langchain-groq"
            return
        try:
            self.model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY, temperature=0.7)
        except Exception as e:
            self._init_error = str(e)
            self.model = None

    def get_response(self, user_input: str, context: Dict = None) -> str:
        self._init_model()
        if self.model is None:
            return f"❌ Model Error: {self._init_error or 'Not initialized'}\n\nSet GROQ_API_KEY in .env file"
        try:
            messages = [SystemMessage(content=self._get_system_prompt())]
            if context:
                messages.append(SystemMessage(content=str(context)))
            messages.append(HumanMessage(content=user_input))
            response = self.model.invoke(messages)
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            return f"Error: {str(e)}"

    def explain_code(self, code: str, detail_level: str = "medium") -> str:
        detail_instructions = {
            "simple": "Explain SIMPLY (for beginners): What does this code do? Line-by-line explanation? What's the output? Key concepts used?",
            "medium": "COMPREHENSIVE: What's the purpose? Line-by-line breakdown? Variable tracking? Input→Output flow? Improvements? Complexity?",
            "detailed": "EXPERT ANALYSIS: Complete walkthrough? Every variable tracked? Data flow? Complexity? Edge cases? Bugs? Best practices? Alternatives?"
        }
        prompt = f"""{detail_instructions.get(detail_level, detail_instructions["medium"])}

ANALYZE THIS EXACT CODE (not generic!):
```python
{code}
```

Show exactly how THIS code works!"""
        return self.get_response(prompt)

    def review_code(self, code: str, expected_behavior: str = None) -> str:
        prompt = f"""YOU ARE A SENIOR PYTHON CODE REVIEWER.

REVIEW THIS EXACT CODE:
```python
{code}
```"""
        if expected_behavior:
            prompt += f"\n\nEXPECTED: {expected_behavior}"
        prompt += """

DETAILED REVIEW:
## ✅ What's Good
- Praise good patterns in THIS code
- Specific lines that are well-written

## ❌ Issues & Bugs
- Specific problems in THIS code
- Show exact lines
- Explain why they're problems

## 🎯 Improvements
- Specific suggestions for THIS code
- Show before/after examples

## 📚 Best Practices
- PEP 8 violations
- Pythonic alternatives for THIS code

## 🔍 Testing
- How to test THIS code
- Edge cases

## ⚡ Performance
- Any performance issues?
- How to optimize THIS code?"""
        return self.get_response(prompt)

    def generate_hint(self, exercise: str, attempt: str = None) -> str:
        prompt = f'EXERCISE: "{exercise}"\n'
        if attempt:
            prompt += f"STUDENT ATTEMPT:\n```python\n{attempt}\n```\nHint for this specific code?"
        else:
            prompt += "Give ONE small hint to get started."
        prompt += "\n\nGive ONE hint only (not the solution!) using Socratic method."
        return self.get_response(prompt)

    def create_custom_exercise(self, topic: str, difficulty: str, weak_areas: List[str] = None) -> str:
        prompt = f"""CREATE A PYTHON EXERCISE:
TOPIC: {topic}
DIFFICULTY: {difficulty}"""
        if weak_areas:
            prompt += f"\nFOCUS ON: {', '.join(weak_areas)}"
        prompt += """

REQUIREMENTS:
1. Real-world scenario
2. Clear requirements
3. 2-3 example inputs/outputs
4. Constraints
5. Starter code (optional)
6. One hint
7. Full solution

Make it practical and interesting!"""
        return self.get_response(prompt)

    def answer_any_python_question(self, question: str) -> str:
        prompt = f"""ANSWER THIS PYTHON QUESTION:
{question}

INCLUDE:
- Direct answer
- Code examples
- Explanation
- Common mistakes
- When to use/not use
- Performance notes
- Related concepts
- Real-world use case

Be thorough but clear!"""
        return self.get_response(prompt)

    def change_teaching_style(self, new_style: str):
        if new_style in ["visual", "verbal", "kinesthetic", "socratic"]:
            self.teaching_style = new_style

# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

tutor = PythonTutor()

# ============================================================================
# WRAPPER FUNCTIONS - THESE ARE REQUIRED FOR IMPORTS
# ============================================================================

def get_response(user_input: str, context: Dict = None) -> str:
    """Wrapper function for get_response"""
    return tutor.get_response(user_input, context)

def explain_code(code: str, detail_level: str = "medium") -> str:
    """Wrapper function for explain_code"""
    return tutor.explain_code(code, detail_level)

def review_code(code: str, expected_behavior: str = None) -> str:
    """Wrapper function for review_code"""
    return tutor.review_code(code, expected_behavior)

def generate_hint(exercise: str, attempt: str = None) -> str:
    """Wrapper function for generate_hint"""
    return tutor.generate_hint(exercise, attempt)

def create_custom_exercise(topic: str, difficulty: str, weak_areas: List[str] = None) -> str:
    """Wrapper function for create_custom_exercise"""
    return tutor.create_custom_exercise(topic, difficulty, weak_areas)

def answer_python_question(question: str) -> str:
    """Wrapper function for answer_python_question"""
    return tutor.answer_any_python_question(question)

def set_teaching_style(new_style: str):
    """Wrapper function for set_teaching_style"""
    tutor.change_teaching_style(new_style)

def model_status() -> Dict[str, str]:
    """Wrapper function for model_status"""
    if tutor.model is not None:
        return {"ready": "yes", "message": "✅ Model ready"}
    if tutor._init_error:
        return {"ready": "no", "message": f"❌ {tutor._init_error}"}
    return {"ready": "no", "message": "⚠️ Model not initialized"}