# 📚 Smart Study Planner

> AI-powered study planner with task management, session tracking, and intelligent study recommendations for students

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 🎯 Project Overview

**Smart Study Planner** is an intelligent, terminal-based study management application designed to help students organize their learning, track study sessions, and receive AI-powered recommendations to optimize their study habits. Built with Python and emphasizing clean architecture, this project demonstrates core computer science concepts including data structures, algorithms, file I/O, and basic machine learning principles.

### Problem Statement

Students often struggle with:
- Managing multiple tasks and assignments with varying priorities
- Tracking study time across different subjects
- Understanding their study patterns and productivity
- Getting personalized recommendations to improve learning efficiency

### Solution

This application provides:
- **Task Management**: Create, organize, and prioritize academic tasks
- **Study Tracking**: Record and analyze study sessions
- **AI Recommendations**: Get intelligent suggestions based on study patterns
- **Progress Visualization**: View statistics and insights

---

## ✨ Features

### 1. Task Management System
- ✅ Create tasks with titles, descriptions, priorities (High/Medium/Low), and due dates
- ✅ View all tasks sorted by priority and completion status
- ✅ Mark tasks as completed
- ✅ Delete tasks
- ✅ Filter high-priority tasks
- ✅ Persistent storage using JSON

### 2. Study Session Tracking
- 📊 Record study sessions with subject and duration
- 📊 Track total study time and session count
- 📊 Calculate average session duration
- 📊 Identify most-studied subjects
- 📊 Data visualization and analytics

### 3. AI-Powered Recommendations
- 🤖 Personalized study tips based on your patterns
- 🤖 Frequency analysis and consistency tracking
- 🤖 Subject diversity recommendations
- 🤖 Optimal study duration suggestions
- 🤖 Evidence-based learning strategies

### 4. User Interface
- 🎨 Clean, intuitive terminal-based interface
- 🎨 Unicode symbols and formatting for better readability
- 🎨 Menu-driven navigation
- 🎨 Input validation and error handling

---

## 📁 Project Structure

```
smart-study-planner/
│
├── main.py                      # Application entry point
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
│
├── src/                          # Source code modules
│   ├── __init__.py               # Package initializer
│   ├── task_manager.py           # Task management logic
│   ├── study_tracker.py          # Study session tracking
│   ├── recommender.py            # AI recommendation engine
│   └── utils.py                  # Utility functions
│
├── data/                         # Application data (auto-generated)
│   ├── tasks.json                # Task storage
│   └── study_sessions.json       # Study session records
│
├── screenshots/                  # Application screenshots
│   └── README.md                 # Screenshot guide
│
└── recordings/                   # Demo videos (optional)
    └── README.md                 # Recording guide
```

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/atharvadwd121-coder/smart-study-planner.git
cd smart-study-planner
```

### Step 2: Install Dependencies

The project uses only Python standard library, so no additional packages are required for basic functionality:

```bash
pip install -r requirements.txt
```

*Note: requirements.txt lists optional dependencies for enhanced features.*

### Step 3: Run the Application

```bash
python main.py
```

---

## 💻 Usage Guide

### Starting the Application

1. Run `python main.py`
2. You'll see the main menu with 9 options

### Main Menu Options

```
1. Add New Task       - Create a new task with priority and due date
2. View All Tasks     - Display all tasks sorted by priority
3. Complete Task      - Mark a task as completed
4. Start Study Session - Log a new study session
5. View Study Statistics - See your study analytics
6. Get AI Recommendations - Receive personalized study tips
7. View Priority Tasks - Filter high-priority tasks
8. Delete Task        - Remove a task permanently
9. Exit               - Close the application
```

### Example Workflow

#### 1. Adding a Task
```
Enter task title: Complete Data Structures Assignment
Enter task description: Implement binary search tree
Select priority (1-3): 1
Enter due date (YYYY-MM-DD): 2025-11-25

✓ Task added successfully! (ID: a3f4b2c1)
```

#### 2. Starting a Study Session
```
Enter subject/topic: Data Structures
Enter planned duration (minutes): 60

✓ Study session started for Data Structures!
Duration: 60 minutes
```

#### 3. Viewing Recommendations
```
--- AI Study Recommendations ---

1. Keep building momentum! Try to study consistently for better retention.
2. Pro tip: Use the Pomodoro Technique - 25 minutes of focused study followed by a 5-minute break.
3. Review your notes within 24 hours of learning for better retention.
```

---

## 🧠 Algorithm Design

### 1. Task Prioritization Algorithm

**Implementation**: `task_manager.py` → `get_all_tasks()`

```python
def get_all_tasks(self):
    return sorted(self.tasks, key=lambda x: (
        x['completed'],  # Incomplete tasks first
        {'High': 0, 'Medium': 1, 'Low': 2}.get(x['priority'], 3)
    ))
```

**Time Complexity**: O(n log n) - uses Python's Timsort algorithm  
**Space Complexity**: O(n) - creates a new sorted list

### 2. Study Pattern Analysis

**Implementation**: `recommender.py` → `get_recommendations()`

**Algorithm Flow**:
1. Retrieve all study sessions
2. Calculate aggregate statistics (total time, average duration)
3. Analyze frequency patterns (daily consistency)
4. Evaluate subject diversity
5. Generate context-aware recommendations

**Time Complexity**: O(n) - single pass through sessions  
**Space Complexity**: O(n) - stores session data

### 3. Data Persistence

**Implementation**: JSON-based file storage

```python
def _save_tasks(self):
    with open(self.data_file, 'w') as f:
        json.dump(self.tasks, f, indent=4)
```

**Benefits**:
- Human-readable format
- Easy debugging and data inspection
- No external database required
- Cross-platform compatibility

---

## 🧪 Testing

### Manual Testing Checklist

- [ ] Create tasks with all priority levels
- [ ] Complete and delete tasks
- [ ] Start multiple study sessions
- [ ] View statistics after several sessions
- [ ] Check AI recommendations with different data patterns
- [ ] Test data persistence (close and reopen app)
- [ ] Validate input handling (invalid dates, empty fields)

### Test Scenarios

**Scenario 1: Task Management**
```
1. Add 3 tasks (High, Medium, Low priority)
2. Complete the Medium priority task
3. View all tasks → Verify sorting
4. Delete the Low priority task
```

**Scenario 2: Study Tracking**
```
1. Record 3 sessions: Math (30 min), Physics (45 min), Math (30 min)
2. View statistics → Verify:
   - Total: 105 minutes (1.75 hours)
   - Average: 35 minutes
   - Most studied: Math
```

**Scenario 3: AI Recommendations**
```
1. With 0 sessions → "Start your learning journey!"
2. With 3 sessions, 1 subject → "Try diversifying your study topics"
3. With 5+ sessions, 3+ subjects → "Great subject diversity!"
```

---

## 🎓 Concepts Demonstrated

### Programming Concepts
- **Object-Oriented Programming**: Classes, inheritance, encapsulation
- **Data Structures**: Lists, dictionaries, JSON
- **File I/O**: Reading/writing JSON files
- **Error Handling**: Try-except blocks, input validation
- **Modular Design**: Separation of concerns, code organization

### Software Engineering
- **Version Control**: Git and GitHub
- **Documentation**: Comprehensive README, code comments
- **Code Style**: PEP 8 compliance, meaningful names
- **Project Structure**: Logical file organization

### Algorithms
- **Sorting**: Priority-based task sorting
- **Search**: Task lookup by ID
- **Statistical Analysis**: Mean, sum, frequency counting
- **Pattern Recognition**: Study habit analysis

---

## 📸 Screenshots

*Screenshots should be added to the `/screenshots` directory*

### Main Menu
![Main Menu](screenshots/main_menu.png)

### Task Management
![Task List](screenshots/view_tasks.png)

### Study Statistics
![Statistics](screenshots/statistics.png)

### AI Recommendations
![Recommendations](screenshots/recommendations.png)

---

## 🔮 Future Enhancements

### Planned Features
- [ ] **Data Visualization**: Charts and graphs using matplotlib
- [ ] **Calendar Integration**: Sync with Google Calendar
- [ ] **Pomodoro Timer**: Built-in timer with breaks
- [ ] **Goal Setting**: Weekly/monthly study goals
- [ ] **Export Reports**: Generate PDF study reports
- [ ] **Mobile App**: Flutter-based mobile version
- [ ] **Web Interface**: Flask web application
- [ ] **Cloud Sync**: Multi-device synchronization

### Technical Improvements
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Unit tests with pytest
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Docker containerization
- [ ] REST API for external integrations

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 style guide
- Add docstrings to all functions
- Write meaningful commit messages
- Update documentation for new features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Atharva Dwivedi**
- GitHub: [@atharvadwd121-coder](https://github.com/atharvadwd121-coder)
- University: VIT Bhopal
- Course: CSE - AI Integrated MTech

---

## 🙏 Acknowledgments

- **Inspiration**: Based on personal experience managing study schedules
- **Python Standard Library**: For providing robust built-in tools
- **MIT OpenCourseWare**: For computer science learning resources
- **VIT Bhopal Faculty**: For project guidance and support

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [documentation](README.md)
2. Open an [issue](https://github.com/atharvadwd121-coder/smart-study-planner/issues)
3. Review existing [issues](https://github.com/atharvadwd121-coder/smart-study-planner/issues)

---

## ⭐ Star This Repository

If you find this project helpful, please consider giving it a star! It helps others discover the project.

---

**Happy Studying! 📚✨**
