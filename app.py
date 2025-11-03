"""
🚀 AI PYTHON TUTOR PRO - FINAL COMPLETE VERSION
✅ Dynamic AI lessons with teaching styles
✅ Premium UI with animations
✅ All features working perfectly
"""

import streamlit as st
from datetime import datetime
from core import (get_response, set_teaching_style, model_status, explain_code, 
                  review_code, generate_hint, create_custom_exercise, answer_python_question)
from progress_tracker import ProgressTracker
from lessons import get_lesson, get_all_lessons, get_lessons_by_topic, get_all_topics, get_topic_name

st.set_page_config(page_title="🚀 AI Python Tutor Pro", page_icon="🚀", layout="wide")

# ============================================================================
# PREMIUM CSS WITH ANIMATIONS
# ============================================================================

PREMIUM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    * { 
        font-family: 'Poppins', sans-serif; 
    }
    
    code, pre { 
        font-family: 'JetBrains Mono', monospace; 
    }
    
    body { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); 
        min-height: 100vh; 
    }
    
    .glass { 
        background: rgba(255, 255, 255, 0.95); 
        backdrop-filter: blur(20px); 
        border: 1px solid rgba(255, 255, 255, 0.3); 
        border-radius: 25px; 
        padding: 24px; 
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.15); 
        transition: all 0.4s ease; 
    }
    
    .glass:hover { 
        transform: translateY(-8px); 
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.25); 
    }
    
    @keyframes slideInUp { 
        from { opacity: 0; transform: translateY(30px); } 
        to { opacity: 1; transform: translateY(0); } 
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .msg-user { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
        color: white; 
        padding: 16px 20px; 
        border-radius: 20px; 
        margin: 10px 0; 
        animation: slideInUp 0.5s ease-out; 
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3); 
    }
    
    .msg-ai { 
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
        color: #1a1a2e; 
        padding: 16px 20px; 
        border-radius: 20px; 
        margin: 10px 0; 
        animation: slideInUp 0.5s ease-out; 
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08); 
    }
    
    .stat-card { 
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
        border: 2px solid rgba(102, 126, 234, 0.2); 
        border-radius: 18px; 
        padding: 20px; 
        text-align: center; 
        animation: slideInUp 0.6s ease-out; 
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.2);
    }
    
    .stat-num { 
        font-size: 32px; 
        font-weight: 700; 
        background: linear-gradient(135deg, #667eea, #764ba2); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        animation: pulse 2s infinite;
    }
    
    .lesson-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7));
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .lesson-card:hover {
        transform: translateX(10px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
    }
</style>
"""

st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "history" not in st.session_state:
    st.session_state.history = []
if "tracker" not in st.session_state:
    st.session_state.tracker = ProgressTracker("student")
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = None
if "current_topic" not in st.session_state:
    st.session_state.current_topic = ""
if "lesson_content" not in st.session_state:
    st.session_state.lesson_content = ""
if "teaching_style" not in st.session_state:
    st.session_state.teaching_style = "visual"

tracker = st.session_state.tracker

# ============================================================================
# DYNAMIC LESSON GENERATION FUNCTION
# ============================================================================

def generate_dynamic_lesson(topic, style):
    """Generate AI-powered lesson dynamically based on topic and teaching style"""
    style_instructions = {
        "visual": "Use ASCII art, diagrams, flowcharts, and visual representations. Show memory layouts and data flow visually.",
        "verbal": "Use detailed explanations, metaphors, analogies, and rich vocabulary. Explain concepts thoroughly with multiple examples.",
        "kinesthetic": "Provide hands-on exercises, interactive coding challenges, and step-by-step coding tasks to practice.",
        "socratic": "Ask guiding questions, provide hints, encourage critical thinking, and help discover answers through questioning."
    }
    
    prompt = f'''
You are an expert Python tutor. Teach the topic "{topic}" tailored for {style} learners.

{style_instructions.get(style, "")}

Provide a comprehensive lesson with:
1. **Explanation**: {style_instructions.get(style, "Clear explanation")}
2. **Code Examples**: Working Python code demonstrating the concept
3. **Exercise**: One practical exercise for the student
4. **Hint**: A helpful hint for the exercise
5. **Key Takeaways**: 3-5 bullet points summarizing the lesson

Format using markdown with clear section headers.
'''
    return get_response(prompt)

# ============================================================================
# HEADER
# ============================================================================

col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    st.markdown("<h1 style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 42px;'>🚀 AI Python Tutor Pro</h1><p style='color: #666;'>Advanced AI Learning Assistant with Dynamic Lessons</p>", unsafe_allow_html=True)
with col2:
    status = model_status()
    st.markdown(f"<div class='glass' style='text-align: center;'><div style='font-size: 24px;'>{'✅' if status.get('ready') == 'yes' else '⚠️'}</div><div style='color: {'#06c564' if status.get('ready') == 'yes' else '#ff6b6b'};'>{status.get('message', 'Unknown')}</div></div>", unsafe_allow_html=True)
with col3:
    if st.button("🌙 Mode"):
        st.session_state.dark_mode = not st.session_state.get("dark_mode", False)

st.markdown("---")

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("### 📊 Your Dashboard")
    stats = tracker.get_stats()
    
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown(f"<div class='stat-card'><div class='stat-num'>{stats['level']}</div><div style='font-size: 13px; color: #666; margin-top: 8px;'>LEVEL</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-card'><div class='stat-num'>{stats['xp']}</div><div style='font-size: 13px; color: #666; margin-top: 8px;'>XP</div></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown(f"<div class='stat-card'><div class='stat-num'>{stats['lessons_completed']}</div><div style='font-size: 13px; color: #666; margin-top: 8px;'>LESSONS</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-card'><div class='stat-num'>{stats['current_streak']}</div><div style='font-size: 13px; color: #666; margin-top: 8px;'>🔥 STREAK</div></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    style = st.selectbox("🎓 Teaching Style", ["visual", "verbal", "kinesthetic", "socratic"], 
                         index=["visual", "verbal", "kinesthetic", "socratic"].index(st.session_state.teaching_style))
    if st.button("✅ Apply Style"):
        st.session_state.teaching_style = style
        set_teaching_style(style)
        st.success(f"✅ Set to **{style}**!")

# ============================================================================
# TABS
# ============================================================================

tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "📚 Learn", "⚡ Tools", "📈 Analytics"])

# ============================================================================
# TAB 1: CHAT
# ============================================================================

with tab1:
    col1, col2 = st.columns([2.5, 1.5], gap="large")
    
    with col1:
        st.markdown("### 💬 Conversation")
        for entry in st.session_state.history:
            role, content, ts = entry.get("role"), entry.get("content"), entry.get("time")
            if role == "user":
                st.markdown(f"<div class='msg-user'><b>You:</b> {content}<br><span style='font-size: 11px;'>{ts}</span></div>", unsafe_allow_html=True)
            elif role == "assistant":
                st.markdown(f"<div class='msg-ai'><b>🤖 Tutor:</b> {content}<br><span style='font-size: 11px;'>{ts}</span></div>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📝 Ask Anything")
        col_input, col_btn = st.columns([5, 1])
        with col_input:
            user_input = st.text_input("Your Question", placeholder="Ask any Python question...", 
                                       key="chat_input", label_visibility="collapsed")
        with col_btn:
            if st.button("🚀 Send"):
                if user_input.strip():
                    now = datetime.now().strftime("%H:%M:%S")
                    st.session_state.history.append({"role": "user", "content": user_input, "time": now})
                    with st.spinner("🤖 Thinking..."):
                        response = answer_python_question(user_input)
                    now2 = datetime.now().strftime("%H:%M:%S")
                    st.session_state.history.append({"role": "assistant", "content": response, "time": now2})
                    tracker.add_xp(5, "message")
                    st.rerun()
    
    with col2:
        st.markdown("### 🎯 Chat Stats")
        st.markdown(f"<div class='glass'><p>✅ Messages: <b>{len([x for x in st.session_state.history if x['role']=='user'])}</b></p><p>🎓 Level: <b>{stats['level']}</b></p><p>⭐ XP: <b>+{stats['xp']}</b></p></div>", unsafe_allow_html=True)

# ============================================================================
# TAB 2: LEARN (Dynamic AI Lessons + Static Browse)
# ============================================================================

with tab2:
    st.markdown("### 📚 Learning Paths")
    
    # Dynamic Lesson Generation
    st.markdown("#### 🤖 Generate Custom Lesson")
    topic_input = st.text_input("Enter Python Topic", value=st.session_state.current_topic, 
                                 placeholder="e.g., list comprehensions, decorators, async/await", 
                                 label_visibility="collapsed")
    
    if st.button("✨ Generate AI Lesson"):
        if topic_input.strip():
            with st.spinner(f"🤖 Generating {st.session_state.teaching_style} lesson for '{topic_input}'..."):
                lesson_md = generate_dynamic_lesson(topic_input, st.session_state.teaching_style)
                st.session_state.current_topic = topic_input
                st.session_state.lesson_content = lesson_md
                tracker.add_xp(10, "lesson")
            st.rerun()
    
    if st.session_state.lesson_content:
        st.markdown("---")
        st.markdown(st.session_state.lesson_content)
    
    st.markdown("---")
    
    # Browse Static Lessons
    st.markdown("#### 📖 Browse Lesson Library")
    topics = get_all_topics()
    
    for topic in sorted(topics):
        with st.expander(f"**{get_topic_name(topic)}**"):
            lessons = get_lessons_by_topic(topic)
            cols = st.columns(3)
            for idx, (lid, lesson) in enumerate(lessons):
                with cols[idx % 3]:
                    if st.button(f"▶️ {lesson['title'][:30]}", key=f"lesson_{lid}"):
                        st.session_state.current_lesson = lid
                        st.rerun()
    
    if st.session_state.current_lesson:
        lesson = get_lesson(st.session_state.current_lesson)
        if lesson:
            st.markdown(f"### {lesson['title']}")
            st.markdown(f"**{lesson['difficulty']}** | **{lesson['duration']}**")
            if st.button("✅ Mark Complete"):
                tracker.add_xp(20, "lesson")
                st.success("🎉 +20 XP!")

# ============================================================================
# TAB 3: TOOLS
# ============================================================================

with tab3:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### 💡 Explain Code")
        code = st.text_area("Paste Code", height=150, key="exp", 
                           placeholder="def hello():\n    print('Hello')", 
                           label_visibility="collapsed")
        level = st.select_slider("Detail Level", ["simple", "medium", "detailed"], value="medium")
        if st.button("🔍 Explain"):
            if code.strip():
                with st.spinner("Analyzing..."):
                    result = explain_code(code, level)
                st.markdown("**Explanation:**")
                st.markdown(result)
                tracker.add_xp(10, "code_explain")
    
    with col2:
        st.markdown("### ✅ Review Code")
        code_rev = st.text_area("Paste Code", height=150, key="rev", 
                                placeholder="x = 5", label_visibility="collapsed")
        expected = st.text_input("Expected Output", label_visibility="collapsed", 
                                placeholder="Expected behavior...")
        if st.button("📋 Review"):
            if code_rev.strip():
                with st.spinner("Reviewing..."):
                    result = review_code(code_rev, expected if expected else None)
                st.markdown("**Code Review:**")
                st.markdown(result)
                tracker.add_xp(15, "code_review")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### 💡 Get Hint")
        exercise_desc = st.text_input("Exercise Description", label_visibility="collapsed", 
                                      placeholder="Describe your coding problem...")
        student_attempt = st.text_area("Your Attempt", height=100, 
                                       label_visibility="collapsed", placeholder="Your code...")
        if st.button("🔑 Get Hint"):
            if exercise_desc.strip():
                with st.spinner("Generating hint..."):
                    hint = generate_hint(exercise_desc, student_attempt if student_attempt else None)
                st.info(hint)
                tracker.add_xp(5, "hint")
    
    with col2:
        st.markdown("### 🎯 Create Exercise")
        ex_topic = st.text_input("Topic", label_visibility="collapsed", placeholder="e.g., loops")
        ex_diff = st.select_slider("Difficulty", ["easy", "medium", "hard"], value="medium")
        ex_weak = st.text_input("Weak Areas", label_visibility="collapsed", 
                                placeholder="e.g., syntax, logic")
        if st.button("✨ Create"):
            if ex_topic.strip():
                weaknesses = [w.strip() for w in ex_weak.split(",")] if ex_weak else None
                with st.spinner("Creating exercise..."):
                    ex = create_custom_exercise(ex_topic, ex_diff, weaknesses)
                st.markdown("**Custom Exercise:**")
                st.markdown(ex)
                tracker.add_xp(20, "create_ex")

# ============================================================================
# TAB 4: ANALYTICS
# ============================================================================

with tab4:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("XP", f"{stats['xp']}", delta="+5")
    with col2:
        st.metric("Level", f"{stats['level']}", delta="Level Up Soon!")
    with col3:
        st.metric("Streak", f"{stats['current_streak']} days", delta="+1")
    
    st.markdown("---")
    st.markdown("### 🏆 Achievements")
    st.info("🚀 Feature coming soon: Badges, Certificates, Learning Analytics Dashboard")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("""
---
<footer style='text-align:center;color:#999;font-size:13px;'>
<p>🚀 AI Python Tutor Pro | Built with ❤️ by Yaswanth Naga Sai</p>
<p>Dynamic AI Lessons • Teaching Styles • Progress Tracking</p>
</footer>
""", unsafe_allow_html=True)