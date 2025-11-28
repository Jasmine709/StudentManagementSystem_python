# Student Management System

**Project Duration:** Sep 2024 – Oct 2024  
**Team Project:** 4 members

## Project Overview  
This project is a small but complete management system written in **Python 3**, designed to simulate how universities manage student accounts and related information.

It includes:

- A **role-based entry** (Student / Admin)
- **Account registration & login**
- **Student information management**
- A **simple GUI front-end** for common operations

## Features

### User Roles

- **Student**
  - Register a new student account  
  - Log in with existing credentials  
  - View and update personal profile information  

- **Administrator**
  - Log in with administrator credentials  
  - View student lists  
  - Edit basic student information  
  - Access student / course management menus  

### Student & Course Management

- Maintain basic student records (ID, name, etc.)  
- Basic course-related structures via:  
  - `subject.py`  
  - `student_course_system.py`  
  - `university_system.py`  
- Data persistence using local files such as `students.data`

### Menu-Driven Flow

- Central **main menu** that supports:
  - Student vs Admin role selection  
  - Registration vs Login  
  - Navigation to student/admin management operations  
- Clear sub-menu design (student system, admin system, course system, etc.)

### GUI Interface

- A **GUI version** implemented in `GUI.py`
- Provides windows/dialogs for:
  - Role selection (Student / Admin)  
  - Login and registration  
  - Student information operations  
- GUI actions are connected to the same underlying logic used in the menu system

## Project Structure

```text
StudentManagementSystem_python/
├── main.py                  # Entry point for the menu/console version
├── GUI.py                   # Entry point for the GUI version
├── admin_system.py          # Admin workflows & operations
├── student_system.py        # Student workflows & operations
├── student_course_system.py # Student–course logic
├── university_system.py     # System coordination & integration
├── student.py               # Student model/class
├── subject.py               # Subject model/class
├── data.py                  # Sample data helpers
├── database.py              # Data persistence & file operations
├── students.data            # Local storage file for student records
├── __init__.py
└── __pycache__/             # Python cache (ignored)

```

## Getting Started

### 1. Requirements  
Python **3.8+**

### 2. Clone the Repository

```bash
git clone https://github.com/Jasmine709/StudentManagementSystem_python.git
cd StudentManagementSystem_python
```

### 3. Run (Menu / Console Version)
python main.py

### 4. Run (GUI Version)
python GUI.py

## My Contributions (Jasmine)

I was responsible for the overall system setup, main menu flow, user management (student & admin), and the GUI implementation.

### 1. System Architecture & Menu Flow

- Designed the structure of the whole project, including how modules such as student_system.py, admin_system.py, student_course_system.py and university_system.py work together.
- Implemented the central menu controller in main.py, handling:
-- Role selection (Student / Admin)
- Navigation between registration, login, and management functions
- Ensured the code is modular so that both the menu version and GUI version can reuse the same logic.

### 2. User Account Management

Implemented complete workflows for both user roles:

#### Student Users
- Student registration with basic validation (ID, name, password, etc.)
- Student login and session-based access to their functions
- Ability to update personal information (e.g. name or password)

#### Administrator Users
- Administrator login flow
- Access to student lists and basic management operations
- Functions to modify student information via admin menus

### 3. Data Handling & Persistence
- Integrated user management with the underlying data layer (data.py, database.py, students.data)
- Implemented:
  - Loading student data at start-up
  - Saving changes after registration or profile updates
  - Basic validation to avoid invalid records

### 4. GUI Development
- Implemented the main GUI front-end in GUI.py, including:
  - Windows / screens for Student vs Admin entry
  - Login and registration forms
  - Buttons and event handlers connected to the underlying systems
- Ensured the GUI is consistent with the menu logic, so the system behaves the same in both modes.
This work provided the core user experience of the system (how users enter, navigate and manage data) and the foundation for other team members to extend features like course/subject management.

