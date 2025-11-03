# Software Requirements Specification (SRS)

## AI Python Tutor Pro

**Version:** 1.0
**Date:** November 1, 2025
**Author:** Yaswanth Naga Sai
**Status:** Final Draft

---

## Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | Oct 15, 2025 | Yaswanth Naga Sai | Initial draft |
| 0.5 | Oct 25, 2025 | Yaswanth Naga Sai | Added use cases and architecture |
| 1.0 | Nov 1, 2025 | Yaswanth Naga Sai | Final version for release |

---

## Table of Contents

1. [Introduction](#1-introduction)
   - 1.1 Purpose
   - 1.2 Scope
   - 1.3 Definitions, Acronyms, and Abbreviations
   - 1.4 References
   - 1.5 Overview
2. [Overall Description](#2-overall-description)
   - 2.1 Product Perspective
   - 2.2 Product Functions
   - 2.3 User Classes and Characteristics
   - 2.4 Operating Environment
   - 2.5 Design and Implementation Constraints
   - 2.6 Assumptions and Dependencies
3. [Functional Requirements](#3-functional-requirements)
4. [External Interface Requirements](#4-external-interface-requirements)
   - 4.1 User Interfaces
   - 4.2 Hardware Interfaces
   - 4.3 Software Interfaces
   - 4.4 Communication Interfaces
5. [Non-Functional Requirements](#5-non-functional-requirements)
   - 5.1 Performance Requirements
   - 5.2 Security Requirements
   - 5.3 Software Quality Attributes
6. [Use Cases](#6-use-cases)
7. [System Architecture](#7-system-architecture)
8. [Acceptance Criteria](#8-acceptance-criteria)
9. [Future Enhancements](#9-future-enhancements)
10. [Approval Signatures](#10-approval-signatures)

---

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) document provides a comprehensive description of the AI Python Tutor Pro application. It details the functional and non-functional requirements, system architecture, and acceptance criteria for the development team, stakeholders, and end users.

The document is intended for:
- Development team members implementing the system
- Quality assurance engineers conducting testing
- Project managers tracking development progress
- Educators and learners evaluating the platform
- Stakeholders making investment decisions

### 1.2 Scope

**Product Name:** AI Python Tutor Pro

**Product Description:** An intelligent, AI-powered Python learning platform that provides personalized education through adaptive teaching styles, interactive code tools, and gamified progress tracking.

**Key Capabilities:**
- Dynamic lesson generation on any Python topic
- Real-time AI chat assistance with voice input support
- Code analysis tools (explainer, reviewer, hint generator, exercise creator)
- Gamified learning with XP, levels, and streak tracking
- Four distinct teaching styles (Visual, Verbal, Kinesthetic, Socratic)
- Static lesson library with pre-built content

**Benefits:**
- Personalized learning experience adapted to individual learning styles
- Instant feedback and guidance on Python concepts
- Engaging gamification to maintain motivation
- Accessible 24/7 learning without human instructor dependency
- Accelerated learning through AI-powered interactions

**Goals:**
- Reduce Python learning curve by 40%
- Achieve 85% user satisfaction rating
- Maintain 70% daily active user retention rate
- Provide sub-10-second AI response times

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| **AI** | Artificial Intelligence |
| **API** | Application Programming Interface |
| **ASCII** | American Standard Code for Information Interchange |
| **DAU** | Daily Active Users |
| **FR** | Functional Requirement |
| **Groq** | AI infrastructure provider offering fast inference |
| **LangChain** | Framework for developing LLM-powered applications |
| **Llama 3.1** | Large Language Model developed by Meta |
| **LLM** | Large Language Model |
| **NFR** | Non-Functional Requirement |
| **RLS** | Row Level Security (database security feature) |
| **SRS** | Software Requirements Specification |
| **UI/UX** | User Interface / User Experience |
| **WebRTC** | Web Real-Time Communication |
| **XP** | Experience Points (gamification metric) |

### 1.4 References

1. IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications
2. Groq API Documentation: https://console.groq.com/docs
3. Streamlit Documentation: https://docs.streamlit.io/
4. LangChain Documentation: https://python.langchain.com/docs/
5. Python PEP 8 Style Guide: https://peps.python.org/pep-0008/

### 1.5 Overview

This SRS is organized according to IEEE 830-1998 standard format. Section 2 provides an overall description of the system, including product perspective, functions, and user characteristics. Section 3 details functional requirements. Section 4 describes external interfaces. Section 5 specifies non-functional requirements. Section 6 presents detailed use cases. Sections 7-9 cover system architecture, acceptance criteria, and future enhancements.

---

## 2. Overall Description

### 2.1 Product Perspective

AI Python Tutor Pro is a standalone web application that operates as a self-contained learning platform. The system integrates with external services while maintaining independence from specific educational institutions.

**System Context:**

```
┌─────────────────────────────────────────────────────┐
│                    End Users                        │
│         (Beginners, Intermediate, Advanced,         │
│                    Educators)                       │
└─────────────────┬───────────────────────────────────┘
                  │
                  │ HTTPS/WebSocket
                  ▼
┌─────────────────────────────────────────────────────┐
│          AI Python Tutor Pro (Streamlit)            │
│  ┌───────────┐  ┌──────────┐  ┌─────────────────┐  │
│  │    UI     │  │  Core    │  │    Progress     │  │
│  │  Layer    │◄─┤  Logic   │◄─┤    Tracker      │  │
│  └───────────┘  └──────────┘  └─────────────────┘  │
│                      │                               │
│                      ▼                               │
│  ┌───────────┐  ┌──────────┐  ┌─────────────────┐  │
│  │ Lessons   │  │Exercises │  │   Visualizer    │  │
│  └───────────┘  └──────────┘  └─────────────────┘  │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ API Calls
                   ▼
┌─────────────────────────────────────────────────────┐
│              External Services                      │
│  ┌─────────────┐         ┌────────────────┐        │
│  │  Groq API   │         │  WebRTC Server │        │
│  │ (Llama 3.1) │         │  (Voice Input) │        │
│  └─────────────┘         └────────────────┘        │
└─────────────────────────────────────────────────────┘
```

**Interface Dependencies:**
- Groq API for AI model inference
- WebRTC for voice input functionality
- Web browser for UI rendering
- File system for session persistence

### 2.2 Product Functions

The system provides the following major functions:

1. **Dynamic Lesson Generation**
   - Generate customized Python lessons on user-specified topics
   - Adapt content to selected teaching style
   - Track lesson completion and award XP

2. **AI-Powered Chat Assistant**
   - Provide instant answers to Python questions
   - Maintain conversation history within sessions
   - Support text and voice input modalities

3. **Code Analysis Tools**
   - Explain Python code with variable detail levels
   - Review code for quality, bugs, and improvements
   - Generate contextual hints for problem-solving
   - Create custom practice exercises

4. **Progress Tracking System**
   - Calculate and award XP for learning activities
   - Manage user levels and progression
   - Track daily learning streaks
   - Display comprehensive statistics

5. **Static Lesson Library**
   - Provide pre-built lesson content
   - Organize lessons by difficulty and topic
   - Enable quick access to common Python concepts

### 2.3 User Classes and Characteristics

| User Class | Description | Expertise Level | Usage Frequency | Technical Comfort |
|------------|-------------|----------------|-----------------|-------------------|
| **Beginners** | New Python learners with little to no programming experience | Low | Daily (30-60 min) | Low to Medium |
| **Intermediate** | Learners with basic Python knowledge seeking to deepen understanding | Medium | 3-4x per week | Medium |
| **Advanced** | Experienced developers using for reference or specialized topics | High | As-needed | High |
| **Educators** | Teachers and instructors using platform for student support | Medium-High | Daily (planning & monitoring) | Medium to High |

**Primary User Persona - "Beginner Learner":**
- Age: 18-35
- Background: Career switcher or student
- Goals: Learn Python fundamentals, build projects
- Frustrations: Complex tutorials, lack of personalized guidance
- Needs: Step-by-step instruction, immediate feedback, motivation

### 2.4 Operating Environment

**Client-Side Requirements:**
- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- Minimum screen resolution: 1024x768 (responsive down to 320px mobile)
- JavaScript enabled
- Microphone access (optional, for voice input)
- Internet connection: 1+ Mbps recommended

**Server-Side Requirements:**
- Python 3.9 or higher
- 2GB RAM minimum, 4GB recommended
- 500MB available disk space
- Linux, Windows, or macOS operating system
- Network access to Groq API endpoints

**Deployment Environment:**
- Cloud-based or on-premises server
- HTTPS protocol (required for WebRTC features)
- Environment variable support (.env files)

### 2.5 Design and Implementation Constraints

**Technical Constraints:**
- Must use Groq API (Llama 3.1-70B or 8B models)
- Built on Streamlit framework (limits real-time features)
- Session-based architecture (state resets on browser refresh)
- API rate limits: 30 requests per minute (Groq free tier)
- No arbitrary code execution for security reasons

**Regulatory Constraints:**
- GDPR compliance for European users (data privacy)
- COPPA compliance if users under 13 (parental consent)
- Accessibility standards (WCAG 2.1 Level AA)

**Business Constraints:**
- Free tier operation (minimize API costs)
- No user registration required (lower barrier to entry)
- Open-source license (MIT)

**Design Standards:**
- Follow PEP 8 Python style guidelines
- Maintain modular architecture for extensibility
- Implement responsive design principles
- Use glassmorphism UI aesthetic

### 2.6 Assumptions and Dependencies

**Assumptions:**
1. Users have reliable internet connectivity
2. Groq API maintains 99% uptime SLA
3. Users access platform via desktop or tablet (mobile is secondary)
4. Most users are English speakers (initial version)
5. Browser permissions granted for voice input (when used)

**Dependencies:**
1. **Groq API Availability:** System requires functioning Groq infrastructure
2. **Streamlit Framework:** Core application dependent on Streamlit library
3. **LangChain Library:** AI orchestration relies on LangChain functionality
4. **Python Ecosystem:** Dependent on Python 3.9+ runtime environment
5. **WebRTC Support:** Voice features require browser WebRTC implementation

---

## 3. Functional Requirements

### FR1: Dynamic Lesson Generation

**Description:** System shall generate customized Python lessons based on user-specified topics and teaching styles.

**Priority:** High

**Inputs:**
- Topic name (string, 3-100 characters)
- Teaching style selection (Visual/Verbal/Kinesthetic/Socratic)

**Processing:**
1. Validate topic input for inappropriate content
2. Construct AI prompt incorporating topic and teaching style
3. Send request to Groq API with Llama 3.1-70B model
4. Parse and format AI response
5. Award +10 XP to user progress

**Outputs:**
- Formatted lesson content (markdown)
- Success/error notification
- Updated XP total

**Error Handling:**
- Empty topic: Display "Please enter a topic" message
- API failure: Show "Unable to generate lesson. Please try again."
- Timeout (>30s): Cancel request and notify user

**Acceptance Criteria:**
- Lesson generated within 10 seconds for 90% of requests
- Content relevant to specified topic (validated by manual review)
- Teaching style correctly applied (distinguishable differences)
- XP awarded upon successful generation

---

### FR2: AI Chat Assistant

**Description:** System shall provide real-time conversational AI assistance for Python questions with optional voice input.

**Priority:** High

**Inputs:**
- User question (text: 1-500 characters, or voice audio)
- Conversation history (previous messages in session)

**Processing:**
1. Transcribe voice input if applicable
2. Append user message to conversation history
3. Construct AI prompt with full conversation context
4. Send request to Groq API with Llama 3.1-8B model (faster)
5. Stream or display AI response
6. Award +5 XP per message
7. Persist conversation in session state

**Outputs:**
- AI response text
- Updated conversation history
- XP notification

**Error Handling:**
- Voice transcription failure: Prompt to retry or use text
- API error: Display previous conversation, show error banner
- Empty input: Disable send button

**Acceptance Criteria:**
- Responses delivered within 5 seconds average
- Conversation history maintained throughout session
- Voice input functional in supported browsers
- Context preserved across multiple messages

---

### FR3: Code Explanation with Detail Levels

**Description:** System shall explain Python code with three selectable detail levels.

**Priority:** High

**Inputs:**
- Python code snippet (1-1000 lines)
- Detail level (Simple/Medium/Detailed)

**Processing:**
1. Validate code for basic Python syntax
2. Select appropriate AI prompt template based on detail level:
   - **Simple:** High-level overview for beginners
   - **Medium:** Line-by-line with key concepts
   - **Detailed:** Comprehensive analysis with edge cases
3. Send code and prompt to Groq API
4. Format response with syntax highlighting
5. Award +10 XP

**Outputs:**
- Formatted explanation (markdown with code blocks)
- Complexity indicators (time/space complexity if applicable)
- XP notification

**Error Handling:**
- Invalid syntax: Attempt explanation with warning
- Code too long: Truncate and notify user
- API failure: Suggest reducing code length and retry

**Acceptance Criteria:**
- All three detail levels produce distinct output
- Explanations accurate for common Python constructs
- Code blocks properly formatted and readable
- Response time <10 seconds for 500-line code

---

### FR4: Code Review with Quality Feedback

**Description:** System shall analyze Python code and provide quality feedback, bug detection, and improvement suggestions.

**Priority:** Medium

**Inputs:**
- Python code snippet (1-1000 lines)
- Expected behavior description (optional, 0-300 characters)

**Processing:**
1. Analyze code for common issues:
   - Syntax errors
   - Logic bugs
   - Performance issues
   - Security vulnerabilities
   - Style violations (PEP 8)
2. Incorporate expected behavior if provided
3. Generate structured feedback:
   - Overall quality score (1-10)
   - Specific issues with line numbers
   - Improvement recommendations
   - Positive aspects (encouragement)
4. Award +15 XP

**Outputs:**
- Quality score
- Categorized feedback (Bugs/Performance/Style/Security)
- Specific recommendations with examples
- XP notification

**Error Handling:**
- Non-Python code: Notify user and reject
- Malicious code patterns: Refuse to review, display warning
- API timeout: Suggest reviewing smaller code sections

**Acceptance Criteria:**
- Detects at least 80% of deliberate test bugs
- Provides actionable feedback (specific, not generic)
- Response time <15 seconds for 500-line code
- Quality score correlates with manual expert review

---

### FR5: Hint Generation

**Description:** System shall generate contextual hints for programming problems without revealing complete solutions.

**Priority:** Medium

**Inputs:**
- Problem description (10-500 characters)
- User's current approach (optional)

**Processing:**
1. Analyze problem to identify key concepts
2. Generate progressive hint (not solution)
3. Focus on methodology, not implementation
4. Award +5 XP

**Outputs:**
- Single contextual hint
- Related Python concepts to research
- XP notification

**Error Handling:**
- Vague problem description: Ask clarifying questions
- API provides full solution: Filter and regenerate hint
- Request fails: Provide generic problem-solving steps

**Acceptance Criteria:**
- Hints do not contain complete solutions
- Provide actionable next steps
- Reference relevant Python concepts
- Generated within 5 seconds

---

### FR6: Custom Exercise Creation

**Description:** System shall generate custom Python practice exercises based on topic and difficulty level.

**Priority:** Medium

**Inputs:**
- Topic/concept (string)
- Difficulty level (Beginner/Intermediate/Advanced)

**Processing:**
1. Construct exercise prompt with topic and difficulty
2. Generate exercise containing:
   - Problem statement
   - Input/output examples
   - Constraints
   - Starter code (optional)
3. Award +20 XP upon generation

**Outputs:**
- Complete exercise specification
- Example test cases
- XP notification

**Error Handling:**
- Unclear topic: Suggest specific Python concepts
- API returns non-exercise content: Regenerate
- Generation fails: Provide manual exercise library link

**Acceptance Criteria:**
- Exercises match specified difficulty level
- Include clear problem statements and examples
- Solvable with standard Python concepts
- Generated within 8 seconds

---

### FR7: XP Reward System

**Description:** System shall award experience points for learning activities and display progress.

**Priority:** High

**Inputs:**
- Activity type (chat/lesson/explain/review/hint/exercise)
- Activity completion status

**Processing:**
1. Validate activity completion
2. Award XP based on activity type:
   - Chat message: +5 XP
   - Lesson view: +10 XP
   - Code explanation: +10 XP
   - Code review: +15 XP
   - Hint request: +5 XP
   - Exercise completion: +20 XP
3. Update total XP in session state
4. Trigger level calculation (FR8)
5. Display XP notification with animation

**Outputs:**
- XP amount earned
- New total XP
- Visual notification

**Error Handling:**
- Negative XP: Reject and log error
- Duplicate award: Prevent via activity tracking
- Integer overflow: Cap at 999,999 XP

**Acceptance Criteria:**
- XP awarded immediately upon completion
- Correct amount for each activity type
- No duplicate awards for same activity
- Visual feedback for every XP gain

---

### FR8: Level Calculation and Streak Tracking

**Description:** System shall calculate user levels, track daily streaks, and display comprehensive statistics.

**Priority:** Medium

**Inputs:**
- Total XP
- Last activity date
- Current date

**Processing:**
1. Calculate level from XP:
   - Level = floor(sqrt(XP / 100)) + 1
   - Cap at Level 50
2. Track streak:
   - Increment if activity today and yesterday
   - Reset if gap > 1 day
   - Store last activity date
3. Calculate statistics:
   - Total lessons completed
   - Total chats
   - Code analyses performed
   - Current level and XP to next level
   - Streak count

**Outputs:**
- Current level
- XP progress to next level (percentage)
- Daily streak count
- Activity statistics

**Error Handling:**
- Date inconsistencies: Use server time
- Streak overflow: Cap at 999 days
- Missing activity data: Initialize to zero

**Acceptance Criteria:**
- Level accurately reflects XP total
- Streak increments daily with activity
- Streak resets after 1-day gap
- Statistics persist within session
- Progress bar updates in real-time

---

## 4. External Interface Requirements

### 4.1 User Interfaces

**UI Architecture:**

The application uses a tabbed interface with four main sections:

```
┌─────────────────────────────────────────────────────────┐
│  AI Python Tutor Pro                    [Level 5] 250 XP │
│  ═══════════════════════════════════════════════════════ │
│                                                           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────────┐  │
│  │ Lessons │ │   Chat  │ │  Tools  │ │   Library    │  │
│  └────┬────┘ └─────────┘ └─────────┘ └──────────────┘  │
│       │                                                   │
│       ▼                                                   │
│  ┌───────────────────────────────────────────────────┐  │
│  │                                                     │  │
│  │             Dynamic Content Area                   │  │
│  │                                                     │  │
│  │           (Changes based on tab)                   │  │
│  │                                                     │  │
│  └───────────────────────────────────────────────────┘  │
│                                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Progress: ████████░░░░░░░  50 XP to Level 6      │  │
│  │  Streak: 🔥 7 days                                 │  │
│  └───────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
```

**UI Components Specification:**

1. **Dynamic Lessons Tab:**
   - Teaching style selector (radio buttons)
   - Topic input field (text input, max 100 chars)
   - Generate button (primary action)
   - Lesson display area (markdown-rendered)
   - Loading animation during generation

2. **AI Chat Tab:**
   - Message history display (scrollable container)
   - Message input field (text area, max 500 chars)
   - Send button
   - Voice input button (optional, if WebRTC available)
   - Conversation clear button

3. **Code Tools Tab:**
   - Tool selector (dropdown or tabs)
   - Code input area (monospace text area)
   - Configuration options (detail level, expected behavior)
   - Analyze/Generate button
   - Results display area
   - Copy to clipboard button

4. **Lesson Library Tab:**
   - Category filter (dropdown)
   - Lesson grid/list view
   - Lesson cards with title, difficulty, duration
   - Search functionality
   - Preview on hover

**UI Design Requirements:**
- Glassmorphism aesthetic (semi-transparent elements, backdrop blur)
- Smooth animations (0.3s transitions)
- Responsive design (mobile: 320px+, tablet: 768px+, desktop: 1024px+)
- Accessible contrast ratios (WCAG AA minimum)
- Loading states for all async operations
- Error messages in non-intrusive notifications

### 4.2 Hardware Interfaces

**Input Devices:**
- Keyboard: Text input, navigation shortcuts
- Mouse/Trackpad: UI interaction, selection
- Microphone: Voice input (optional, WebRTC-enabled browsers)
- Touchscreen: Mobile and tablet interaction support

**Output Devices:**
- Display: Minimum 1024x768 resolution, color depth 16-bit+
- Speakers/Headphones: Audio feedback for voice input confirmation (optional)

**No Special Hardware Required:** Standard consumer computing devices sufficient.

### 4.3 Software Interfaces

#### 4.3.1 Groq API Interface

**Purpose:** AI model inference for lesson generation, chat, code analysis

**Interface Type:** RESTful HTTP API

**Connection Details:**
- Base URL: `https://api.groq.com/openai/v1/`
- Authentication: Bearer token (API key in headers)
- Protocol: HTTPS
- Data Format: JSON

**API Endpoints Used:**
- `POST /chat/completions`: All AI interactions

**Request Format:**
```json
{
  "model": "llama-3.1-70b-versatile",
  "messages": [
    {"role": "system", "content": "You are a Python tutor..."},
    {"role": "user", "content": "Explain list comprehensions"}
  ],
  "temperature": 0.7,
  "max_tokens": 2048
}
```

**Response Format:**
```json
{
  "id": "chatcmpl-...",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "List comprehensions are..."
      }
    }
  ]
}
```

**Error Handling:**
- HTTP 401: Invalid API key
- HTTP 429: Rate limit exceeded
- HTTP 500: Server error
- Network timeout: Retry with exponential backoff

**Models Used:**
- `llama-3.1-70b-versatile`: Lessons, code review (accuracy priority)
- `llama-3.1-8b-instant`: Chat (speed priority)

#### 4.3.2 Streamlit Framework

**Purpose:** Web application framework and UI rendering

**Interface Type:** Python library import

**Key Modules:**
- `streamlit`: Core UI components
- `streamlit.session_state`: State management
- `streamlit.tabs`: Tab navigation
- `streamlit.cache_data`: Response caching

**Data Flow:**
- Python functions render UI components
- User interactions trigger reruns
- Session state persists between reruns

#### 4.3.3 LangChain Library

**Purpose:** AI orchestration and prompt management

**Interface Type:** Python library import

**Key Components:**
- `ChatGroq`: Groq API wrapper
- `ChatPromptTemplate`: Prompt construction
- `SystemMessage/HumanMessage`: Message formatting

#### 4.3.4 WebRTC (via streamlit-webrtc)

**Purpose:** Voice input capture

**Interface Type:** Browser API via Streamlit component

**Functionality:**
- Audio stream capture
- Real-time transcription (browser-based)
- Microphone permission handling

### 4.4 Communication Interfaces

**Network Protocols:**
- HTTPS (TCP/IP): All API communications
- WebSocket (optional): Streamlit live updates
- WebRTC: Peer-to-peer voice communication

**Data Exchange Format:**
- JSON: API requests/responses
- Markdown: Lesson and explanation content
- Plain text: Chat messages

**Security:**
- TLS 1.2+ encryption for all API calls
- API keys stored in environment variables (never in code)
- CORS headers configured for web deployment

---

## 5. Non-Functional Requirements

### 5.1 Performance Requirements

**Response Time:**
- **PR1:** AI chat responses shall be delivered within 5 seconds average (90th percentile <8s)
- **PR2:** Lesson generation shall complete within 10 seconds (90th percentile <15s)
- **PR3:** Code explanation shall complete within 10 seconds for 500 lines of code
- **PR4:** UI interactions (button clicks, tab switches) shall respond within 100ms
- **PR5:** Page load time shall not exceed 3 seconds on 5 Mbps connection

**Throughput:**
- **PR6:** System shall support up to 100 concurrent users per server instance
- **PR7:** Groq API rate limit of 30 requests/minute shall not be exceeded

**Resource Utilization:**
- **PR8:** Browser memory usage shall not exceed 500MB after 1 hour of use
- **PR9:** Server memory footprint shall not exceed 2GB under normal load
- **PR10:** Session state storage shall not exceed 10MB per user

### 5.2 Security Requirements

**Authentication:**
- **SR1:** System shall not require user authentication for MVP (barrier reduction)
- **SR2:** API keys shall be stored exclusively in `.env` files (never in source code)
- **SR3:** API keys shall never be transmitted to client browsers

**Data Protection:**
- **SR4:** All API communications shall use HTTPS encryption
- **SR5:** User input shall be sanitized to prevent injection attacks
- **SR6:** System shall not execute arbitrary user-provided Python code
- **SR7:** Session data shall be isolated between users (no cross-contamination)

**Privacy:**
- **SR8:** No personally identifiable information (PII) shall be collected
- **SR9:** Conversation history shall only persist during active session
- **SR10:** No data shall be transmitted to third parties beyond Groq API

**Access Control:**
- **SR11:** `.env` files shall have restrictive file permissions (600 on Unix)
- **SR12:** Server endpoints shall validate all input parameters

### 5.3 Software Quality Attributes

#### 5.3.1 Usability

- **UA1:** New users shall be able to generate their first lesson within 2 minutes without instructions
- **UA2:** All error messages shall be displayed in plain English with actionable guidance
- **UA3:** UI shall maintain consistent navigation patterns across all tabs
- **UA4:** Color contrast shall meet WCAG 2.1 Level AA standards (4.5:1 minimum)
- **UA5:** Font sizes shall be adjustable via browser zoom without breaking layout

#### 5.3.2 Reliability

- **RA1:** System shall gracefully handle Groq API failures with informative error messages
- **RA2:** Session state shall persist across tab navigation within same session
- **RA3:** System uptime shall be 99.5% (excluding scheduled maintenance)
- **RA4:** Failed API requests shall implement exponential backoff retry (max 3 attempts)

#### 5.3.3 Maintainability

- **MA1:** All functions shall include docstrings following Google style
- **MA2:** Code shall follow PEP 8 style guidelines (verified via linting)
- **MA3:** System architecture shall be modular (max 300 lines per file recommended)
- **MA4:** Configuration shall be externalized to `config.py` (no hardcoded values)
- **MA5:** Dependencies shall be pinned to specific versions in `requirements.txt`

#### 5.3.4 Portability

- **PA1:** System shall run on Windows, macOS, and Linux without modification
- **PA2:** UI shall render correctly in Chrome, Firefox, Safari, Edge (latest 2 versions)
- **PA3:** No platform-specific dependencies beyond standard Python libraries
- **PA4:** System shall be deployable to cloud platforms (Streamlit Cloud, AWS, Azure, GCP)

#### 5.3.5 Scalability

- **SA1:** Architecture shall support horizontal scaling by adding server instances
- **SA2:** Session state design shall accommodate future database migration
- **SA3:** Codebase shall support adding new teaching styles without core refactoring
- **SA4:** UI framework shall accommodate adding new tabs/features modularly

---

## 6. Use Cases

### Use Case 1: Generate Custom Lesson

**UC-01: Generate Custom Lesson**

**Actor:** Learner (Beginner/Intermediate/Advanced)

**Preconditions:**
- User has accessed the application
- User is on Dynamic Lessons tab
- Groq API is available

**Main Flow:**
1. User selects preferred teaching style (Visual/Verbal/Kinesthetic/Socratic)
2. User enters Python topic in text input field (e.g., "lambda functions")
3. User clicks "Generate Lesson" button
4. System validates topic is not empty
5. System constructs AI prompt incorporating topic and teaching style
6. System sends request to Groq API (llama-3.1-70b-versatile)
7. System displays loading animation
8. System receives lesson content from API
9. System formats content as markdown
10. System displays lesson in content area
11. System awards +10 XP to user
12. System displays XP notification with animation
13. System updates progress bar and level display

**Alternate Flows:**

**3a. User enters empty topic:**
- 3a1. System disables "Generate Lesson" button
- 3a2. System displays hint text "Enter a Python topic to get started"

**6a. API request fails:**
- 6a1. System displays error notification "Unable to generate lesson. Please check your connection and try again."
- 6a2. System logs error details for debugging
- 6a3. System returns to step 2 (user can retry)

**6b. API request times out (>30 seconds):**
- 6b1. System cancels request
- 6b2. System displays notification "Request timed out. Try a more specific topic."
- 6b3. System returns to step 2

**Postconditions:**
- Lesson displayed in UI
- +10 XP added to user total
- Level potentially increased if XP threshold crossed
- Lesson available for viewing until session ends

**Special Requirements:**
- Response time <10 seconds for 90% of requests
- Lesson content must be relevant to specified topic
- Teaching style differences must be distinguishable

---

### Use Case 2: Get Code Review

**UC-02: Get Code Review**

**Actor:** Learner (Any level)

**Preconditions:**
- User has accessed the application
- User is on Code Tools tab
- User has selected "Code Reviewer" tool
- User has Python code to review

**Main Flow:**
1. User pastes Python code into code input area (up to 1000 lines)
2. User optionally enters expected behavior description
3. User clicks "Review Code" button
4. System validates code is not empty
5. System performs basic syntax validation
6. System constructs review prompt with code and expected behavior
7. System sends request to Groq API
8. System displays loading spinner
9. System receives review feedback from API
10. System parses feedback into categories (Bugs/Performance/Style/Security)
11. System extracts quality score (1-10)
12. System displays formatted review:
    - Overall quality score with visual indicator
    - Categorized issues with line numbers
    - Specific recommendations
    - Positive aspects (encouragement)
13. System awards +15 XP to user
14. System displays XP notification
15. System provides "Copy Review" button

**Alternate Flows:**

**4a. Code input is empty:**
- 4a1. System disables "Review Code" button
- 4a2. System displays placeholder text in input area

**5a. Code contains non-Python syntax:**
- 5a1. System displays warning "This doesn't appear to be Python code. Review may be inaccurate."
- 5a2. System continues with review (best effort)

**5b. Code is too long (>1000 lines):**
- 5b1. System displays error "Code exceeds 1000 lines. Please review in smaller sections."
- 5b2. System does not proceed with review
- 5b3. System returns to step 1

**7a. API request fails:**
- 7a1. System displays error notification with retry button
- 7a2. System suggests reviewing smaller code sections
- 7a3. No XP awarded
- 7a4. System returns to step 3

**5c. Malicious code patterns detected:**
- 5c1. System refuses to review
- 5c2. System displays warning "Unable to review code containing potentially harmful operations."
- 5c3. System logs incident for security monitoring
- 5c4. No XP awarded

**Postconditions:**
- Code review displayed with structured feedback
- +15 XP added to user total (if successful)
- Review can be copied to clipboard
- Original code preserved in input area for editing

**Special Requirements:**
- Must detect at least 80% of deliberate test bugs
- Response time <15 seconds for 500-line code
- Quality score should correlate with expert review
- Feedback must be specific and actionable

---

### Use Case 3: Chat with AI Assistant

**UC-03: Chat with AI Assistant**

**Actor:** Learner (Any level)

**Preconditions:**
- User has accessed the application
- User is on AI Chat tab
- Groq API is available

**Main Flow:**
1. User types Python question in chat input field (up to 500 characters)
2. User presses Enter or clicks Send button
3. System validates message is not empty
4. System appends user message to conversation history
5. System displays user message in chat area
6. System constructs AI prompt with full conversation context
7. System sends request to Groq API (llama-3.1-8b-instant for speed)
8. System displays "AI is typing..." indicator
9. System receives AI response
10. System appends AI response to conversation history
11. System displays AI response in chat area with formatting
12. System awards +5 XP to user
13. System displays brief XP notification
14. User can continue conversation from step 1

**Alternate Flows:**

**1a. User clicks voice input button:**
- 1a1. System checks for microphone permissions
- 1a2. System activates WebRTC audio capture
- 1a3. System displays recording indicator
- 1a4. User speaks question
- 1a5. User clicks stop recording button
- 1a6. System transcribes audio to text
- 1a7. System populates input field with transcribed text
- 1a8. Continue to step 2

**1a2a. Microphone permission denied:**
- 1a2a1. System displays notification "Microphone access required for voice input"
- 1a2a2. System provides instructions for granting permission
- 1a2a3. User continues with text input

**1a6a. Transcription fails:**
- 1a6a1. System displays error "Unable to transcribe audio. Please try again or use text input."
- 1a6a2. System clears recording
- 1a6a3. Return to step 1

**7a. API request fails:**
- 7a1. System displays error message in chat "Sorry, I'm having trouble connecting. Please try again."
- 7a2. System preserves conversation history
- 7a3. No XP awarded
- 7a4. User can retry from step 1

**7b. API rate limit exceeded:**
- 7b1. System displays notification "Too many requests. Please wait a moment and try again."
- 7b2. System implements exponential backoff
- 7b3. User can retry after cooldown period

**At any point: User clicks "Clear Conversation" button:**
- System prompts for confirmation
- If confirmed, system clears conversation history
- Chat area resets to welcome message

**Postconditions:**
- Conversation history updated with user question and AI response
- +5 XP added to user total
- Chat scrolled to show latest messages
- Input field cleared and focused for next question
- Full conversation context available for follow-up questions

**Special Requirements:**
- Average response time <5 seconds
- Conversation history persists throughout session
- Voice input functional in Chrome, Edge (WebRTC support)
- Context preserved across multiple exchanges

---

### Use Case 4: Track Learning Progress

**UC-04: Track Learning Progress**

**Actor:** Learner (Any level)

**Preconditions:**
- User has accessed the application
- User has performed at least one XP-earning activity

**Main Flow:**
1. User completes an activity (lesson, chat, code tool)
2. System calculates XP award based on activity type
3. System adds XP to user's total in session state
4. System calculates new level: `level = floor(sqrt(total_xp / 100)) + 1`
5. System checks if level increased
6. If level increased:
   - System displays level-up animation
   - System displays congratulatory notification
7. System updates progress bar showing XP to next level
8. System checks last activity date
9. If activity is consecutive day:
   - System increments streak counter
   - System displays streak notification with fire emoji
10. If streak was broken (gap > 1 day):
    - System resets streak to 1
    - System displays "Welcome back!" notification
11. System updates last activity date to today
12. System displays updated statistics:
    - Current level and XP
    - XP needed for next level
    - Current streak
    - Total activities completed

**Alternate Flows:**

**User views progress at any time:**
- Progress bar always visible at bottom of screen
- Level and current XP displayed in header
- Streak indicator visible in sidebar

**User completes multiple activities rapidly:**
- System queues XP notifications to avoid overlap
- System batches level calculations for performance

**5a. User reaches level cap (Level 50):**
- 5a1. System displays "Max Level Achieved!" notification
- 5a2. System continues tracking XP but does not increase level
- 5a3. System displays total XP without "XP to next level"

**8a. System detects date inconsistency:**
- 8a1. System uses server time as source of truth
- 8a2. System logs inconsistency for debugging

**Postconditions:**
- XP total updated and persisted in session
- Level accurately reflects XP total
- Streak accurately reflects consecutive activity days
- Statistics displayed in UI
- Progress visualization updated

**Special Requirements:**
- XP calculations must be accurate (no duplicate awards)
- Level formula must be consistent across sessions
- Streak logic must handle timezone differences gracefully
- Progress bar updates must be smooth (animated)

---

## 7. System Architecture

### 7.1 High-Level Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                        │
│  ┌──────────────────────────────────────────────────────┐    │
│  │              Streamlit Web Interface                  │    │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌──────────────┐  │    │
│  │  │Lessons │ │  Chat  │ │ Tools  │ │   Library    │  │    │
│  │  │  Tab   │ │  Tab   │ │  Tab   │ │     Tab      │  │    │
│  │  └───┬────┘ └───┬────┘ └───┬────┘ └──────┬───────┘  │    │
│  └──────┼──────────┼──────────┼──────────────┼──────────┘    │
│         │          │          │              │                │
└─────────┼──────────┼──────────┼──────────────┼────────────────┘
          │          │          │              │
          ▼          ▼          ▼              ▼
┌───────────────────────────────────────────────────────────────┐
│                      BUSINESS LOGIC LAYER                     │
│  ┌──────────────────────────────────────────────────────┐    │
│  │                   app.py (Main Controller)            │    │
│  └──────────────────────────────────────────────────────┘    │
│         │                    │                    │           │
│         ▼                    ▼                    ▼           │
│  ┌──────────┐        ┌──────────┐        ┌──────────────┐   │
│  │ core.py  │        │lessons.py│        │ exercises.py │   │
│  │ (AI      │        │ (Lesson  │        │ (Exercise    │   │
│  │ Engine)  │        │ Library) │        │ Generator)   │   │
│  └────┬─────┘        └──────────┘        └──────────────┘   │
│       │                                                       │
│       │              ┌────────────────┐                      │
│       └─────────────►│ visualizer.py  │                      │
│                      │ (Code Display) │                      │
│                      └────────────────┘                      │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           progress_tracker.py (State Manager)         │   │
│  │  ┌─────────┐  ┌──────────┐  ┌─────────────────────┐ │   │
│  │  │   XP    │  │  Level   │  │  Streak & Stats     │ │   │
│  │  │ Manager │  │Calculator│  │    Tracker          │ │   │
│  │  └─────────┘  └──────────┘  └─────────────────────┘ │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────┘
          │                                       │
          ▼                                       ▼
┌───────────────────────────────────────────────────────────────┐
│                     EXTERNAL SERVICES                         │
│  ┌─────────────────────┐         ┌──────────────────────┐    │
│  │   Groq API          │         │   WebRTC Server      │    │
│  │   (Llama 3.1)       │         │   (Voice Input)      │    │
│  │ ┌─────────────────┐ │         │ ┌──────────────────┐ │    │
│  │ │ llama-3.1-70b   │ │         │ │ Audio Capture    │ │    │
│  │ │   (Lessons)     │ │         │ │ & Transcription  │ │    │
│  │ └─────────────────┘ │         │ └──────────────────┘ │    │
│  │ ┌─────────────────┐ │         └──────────────────────┘    │
│  │ │ llama-3.1-8b    │ │                                      │
│  │ │    (Chat)       │ │                                      │
│  │ └─────────────────┘ │                                      │
│  └─────────────────────┘                                      │
└───────────────────────────────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────────────────────────────┐
│                       DATA LAYER                              │
│  ┌──────────────────┐         ┌──────────────────────┐       │
│  │  Session State   │         │    Configuration     │       │
│  │  (In-Memory)     │         │    (.env file)       │       │
│  │ ┌──────────────┐ │         │ ┌──────────────────┐ │       │
│  │ │ User Progress│ │         │ │   API Keys       │ │       │
│  │ │ Chat History │ │         │ │   Settings       │ │       │
│  │ │ XP & Levels  │ │         │ └──────────────────┘ │       │
│  │ └──────────────┘ │         └──────────────────────┘       │
│  └──────────────────┘                                         │
└───────────────────────────────────────────────────────────────┘
```

### 7.2 Component Descriptions

**Presentation Layer:**
- Streamlit web interface providing tabbed navigation
- Renders dynamic content based on user interactions
- Handles user input validation and display formatting

**Business Logic Layer:**
- `app.py`: Main controller orchestrating all features
- `core.py`: AI model interaction and prompt engineering
- `lessons.py`: Static lesson content and organization
- `exercises.py`: Dynamic exercise generation logic
- `visualizer.py`: Code syntax highlighting and formatting
- `progress_tracker.py`: XP, level, and streak management

**External Services:**
- Groq API: AI inference for all natural language tasks
- WebRTC: Voice input capture and transcription

**Data Layer:**
- Streamlit Session State: Temporary user progress storage
- `.env` file: Configuration and API credentials

### 7.3 Data Flow Example (Generate Lesson)

```
User Input (Topic)
      │
      ▼
[app.py: Validate Input]
      │
      ▼
[core.py: Construct Prompt]
      │
      ▼
[Groq API: Generate Content]
      │
      ▼
[core.py: Parse Response]
      │
      ▼
[visualizer.py: Format Markdown]
      │
      ▼
[app.py: Display Lesson]
      │
      ▼
[progress_tracker.py: Award +10 XP]
      │
      ▼
[Session State: Update Totals]
      │
      ▼
[app.py: Show XP Notification]
```

### 7.4 Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Streamlit | Web UI framework |
| Backend | Python 3.9+ | Application logic |
| AI Model | Llama 3.1 (70B/8B) | Natural language processing |
| AI API | Groq | Fast inference infrastructure |
| Voice | streamlit-webrtc | Voice input capture |
| Orchestration | LangChain | AI prompt management |
| Configuration | python-dotenv | Environment variable management |
| State | Streamlit Session State | User progress persistence |

---

## 8. Acceptance Criteria

The following criteria must be met for the system to be considered complete and ready for release:

### 8.1 Functional Acceptance Criteria

- [ ] **AC1:** Dynamic lesson generation produces relevant content for at least 20 diverse Python topics tested
- [ ] **AC2:** All four teaching styles (Visual, Verbal, Kinesthetic, Socratic) produce distinguishably different lessons
- [ ] **AC3:** AI chat maintains conversation context across at least 10 consecutive messages
- [ ] **AC4:** Code explainer correctly explains at least 90% of test code snippets
- [ ] **AC5:** Code reviewer detects at least 80% of deliberately introduced bugs in test suite
- [ ] **AC6:** Hint generator provides hints without revealing complete solutions in 95% of cases
- [ ] **AC7:** Exercise creator generates solvable exercises for all three difficulty levels
- [ ] **AC8:** XP system awards correct amounts for all activity types without duplicates
- [ ] **AC9:** Level calculation formula produces consistent results across sessions
- [ ] **AC10:** Streak tracking correctly increments for consecutive days and resets after gaps
- [ ] **AC11:** Static lesson library contains at least 30 pre-built lessons across all topics
- [ ] **AC12:** Voice input successfully transcribes clear speech in supported browsers

### 8.2 Performance Acceptance Criteria

- [ ] **AC13:** 90% of AI chat responses delivered within 5 seconds
- [ ] **AC14:** 90% of lesson generations complete within 10 seconds
- [ ] **AC15:** UI interactions respond within 100ms on standard hardware
- [ ] **AC16:** Page loads within 3 seconds on 5 Mbps connection
- [ ] **AC17:** Browser memory usage stays below 500MB after 1 hour of continuous use
- [ ] **AC18:** System supports 100 concurrent users per server instance without degradation

### 8.3 Security Acceptance Criteria

- [ ] **AC19:** API keys never exposed in client-side code (verified by code review)
- [ ] **AC20:** All API communications use HTTPS encryption
- [ ] **AC21:** User input sanitization prevents injection attacks (verified by security testing)
- [ ] **AC22:** No arbitrary code execution possible (verified by penetration testing)
- [ ] **AC23:** Session data isolated between users (verified by concurrent user testing)

### 8.4 Usability Acceptance Criteria

- [ ] **AC24:** 80% of test users generate first lesson within 2 minutes without instructions
- [ ] **AC25:** All error messages use plain English and provide actionable guidance
- [ ] **AC26:** Color contrast meets WCAG 2.1 Level AA standards (verified by automated tools)
- [ ] **AC27:** UI renders correctly on mobile (320px), tablet (768px), and desktop (1024px+)
- [ ] **AC28:** Navigation consistent across all four tabs

### 8.5 Reliability Acceptance Criteria

- [ ] **AC29:** Graceful handling of API failures with informative errors (tested with simulated outages)
- [ ] **AC30:** Session state persists across tab navigation within same session
- [ ] **AC31:** Failed API requests retry with exponential backoff (max 3 attempts)
- [ ] **AC32:** System recovers automatically from transient network errors

### 8.6 Code Quality Acceptance Criteria

- [ ] **AC33:** All functions include docstrings following Google style
- [ ] **AC34:** Code passes PEP 8 linting with zero errors
- [ ] **AC35:** No file exceeds 500 lines (recommended max 300 lines)
- [ ] **AC36:** All configuration externalized to `config.py` (no hardcoded values)
- [ ] **AC37:** Dependencies pinned to specific versions in `requirements.txt`

### 8.7 Deployment Acceptance Criteria

- [ ] **AC38:** System runs on Windows, macOS, and Linux without modification
- [ ] **AC39:** Installation completes successfully following README instructions
- [ ] **AC40:** Application deploys to Streamlit Cloud without errors
- [ ] **AC41:** All required environment variables documented in `.env.example`

---

## 9. Future Enhancements

The following features are planned for future releases beyond version 1.0:

### 9.1 Short-Term Enhancements (v1.1 - v1.3)

**Authentication & Profiles (v1.1)**
- User registration and login system
- Persistent progress across devices
- Profile customization (avatar, preferences)
- Social sign-in (Google, GitHub)

**Enhanced Code Playground (v1.2)**
- Integrated code editor with syntax highlighting
- Real-time code execution in sandboxed environment
- Support for Python libraries (NumPy, Pandas, etc.)
- Code sharing via unique URLs

**Expanded Content Library (v1.3)**
- 100+ pre-built lessons
- Video tutorial integration
- Interactive quizzes and assessments
- Downloadable cheat sheets and references

### 9.2 Medium-Term Enhancements (v2.0 - v2.5)

**Multi-Language Support (v2.0)**
- JavaScript, Java, C++, Go language options
- Cross-language comparison features
- Language-specific best practices

**Peer Learning Features (v2.1)**
- Live pair programming sessions
- Code review exchange with other learners
- Discussion forums for each topic
- Mentor matching system

**Advanced Analytics (v2.2)**
- Detailed learning analytics dashboard
- Strengths and weaknesses identification
- Personalized learning path recommendations
- Time-to-mastery predictions

**Certification System (v2.3)**
- Skill-based assessments
- Official completion certificates
- LinkedIn integration for credential sharing
- Employer verification portal

**Mobile Applications (v2.4)**
- Native iOS app
- Native Android app
- Offline lesson access
- Push notifications for streak reminders

**AI Voice Tutor (v2.5)**
- Text-to-speech for lesson narration
- Voice-based conversational learning
- Pronunciation and verbal explanation practice

### 9.3 Long-Term Enhancements (v3.0+)

**Enterprise Features (v3.0)**
- Team management for educators
- Classroom integration (Google Classroom, Canvas)
- Student progress dashboards for teachers
- Custom content creation tools
- SCORM compliance for LMS integration

**Adaptive Learning AI (v3.1)**
- Machine learning-based difficulty adjustment
- Predictive hint generation
- Personalized lesson sequencing
- Learning style auto-detection

**Gamification Expansion (v3.2)**
- Global leaderboards
- Achievement badges and trophies
- Team competitions and challenges
- Virtual currency and rewards shop

**Extended Language Support (v3.3)**
- Interface localization (Spanish, French, German, Chinese, Hindi)
- Culture-specific examples and metaphors
- Regional teaching style preferences

**IDE Integrations (v3.4)**
- VS Code extension
- PyCharm plugin
- Jupyter Notebook integration
- GitHub Copilot-style inline assistance

**Video Content Generation (v3.5)**
- AI-generated video tutorials
- Animated concept visualizations
- Screen recording integration for code walkthroughs

### 9.4 Research & Experimental Features

**Virtual Reality Learning (Research)**
- VR environment for immersive coding
- 3D visualization of data structures
- Virtual classroom experiences

**Quantum Computing Module (Research)**
- Introduction to quantum programming (Qiskit)
- Quantum algorithm tutorials
- Hybrid classical-quantum exercises

**Neurofeedback Integration (Research)**
- EEG-based attention monitoring
- Adaptive difficulty based on cognitive load
- Optimal learning time recommendations

---

## 10. Approval Signatures

This Software Requirements Specification represents the agreed-upon requirements for AI Python Tutor Pro version 1.0.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Project Sponsor** | _________________ | _________________ | __________ |
| **Product Owner** | Yaswanth Naga Sai | _________________ | Nov 1, 2025 |
| **Lead Developer** | _________________ | _________________ | __________ |
| **QA Lead** | _________________ | _________________ | __________ |
| **UX Designer** | _________________ | _________________ | __________ |
| **Technical Architect** | _________________ | _________________ | __________ |

---

**Document Control:**
- **Version:** 1.0
- **Status:** Final Draft
- **Classification:** Internal Use
- **Next Review Date:** February 1, 2026

---

**End of Software Requirements Specification**
