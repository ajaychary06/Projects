
# University Academic Programs Portal

> A Flask-based web application for managing university academic programs and student enrollments with CRUD operations.

## Overview

This web application serves as a comprehensive university portal that enables prospective students to browse and apply to academic programs while allowing universities to manage their program offerings. Built with Flask and SQLAlchemy, it provides a robust platform for educational institution management.

### Key Features
- Student management system with CRUD operations
- University and program information management
- User-friendly web interface
- SQLite database integration
- Responsive design for multiple devices

## Technologies Used
- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/ajaychary06/Projects.git
cd Projects/Advanced-Database-Systems/application.py

```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask flask-sqlalchemy
```

4. Initialize the database:
```bash
python application.py
```

## Usage

1. Start the application:
```bash
python application.py
```

2. Open a web browser and navigate to:
```
http://localhost:5000
```

3. Available operations:
   - Add/Edit/Delete students
   - Add/Edit/Delete university programs
   - View all records

## Developer Guide

### Project Structure
```
Final-proj-ADBS/
├── application.py
├── templates/
│   ├── index.html
│   ├── edit_student.html
│   └── edit_university.html
└── instance/
    └── site.db
```

### Development Setup
1. Fork the repository
2. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

### Database Schema
```python
class University:
    id: Integer (Primary Key)
    name: String(100)
    program_name: String(100)

class Student:
    id: Integer (Primary Key)
    name: String(100)
    course_id: Integer
```

## Expectations

### Performance
- Quick response time (< 2 seconds) for CRUD operations
- Smooth handling of concurrent users
- Efficient database queries

### Limitations
- Basic authentication system
- Limited to SQLite database
- Simple UI design

### Future Enhancements
- Advanced search capabilities
- User authentication and authorization
- RESTful API implementation
- Enhanced UI/UX design
- Support for additional database systems






## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ajaychary06/Projects/blob/main/LICENSE) file for details.


## Contact

Your Name - [@Ajaychary Kandukuri](www.linkedin.com/in/ajaychary-kandukuri-053a5a25a) - ajaycharykandukuri0629@gmail.com


