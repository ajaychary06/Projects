
# Healthcare Data Management System

A secure Flask-based healthcare data management system with role-based access control and encryption capabilities.

## Overview

This project implements a healthcare data management system with encrypted data storage, user authentication, and role-based access control. It's designed for healthcare providers (H) and researchers (R) to securely access and manage patient data.

**Key Features:**
- Role-based access control (Healthcare providers and Researchers)
- AES-256 and RSA-2048 encryption for sensitive data
- Secure password hashing using SHA-256
- MySQL database integration
- Session-based authentication
- CRUD operations for healthcare providers
- Limited data access for researchers

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/ajaychary06/Projects.git
cd Projects/Data-Security-and-Privacy/
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask pymysql cryptography
```

4. Configure MySQL:
- Create a MySQL user
- Update database connection details in `app.py` and `database_setup.py`

5. Initialize the database:
```bash
python database_setup.py
```

6. Run the application:
```bash
python app.py
```

## Developer Guide

### Project Structure
```
healthcare-data-management/
├── app.py                 # Main Flask application
├── database_setup.py      # Database initialization script
├── templates/            # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── query.html
├── static/              # Static files (CSS, JS)
└── keys/               # Generated encryption keys
```

### Security Implementation

1. **Encryption:**
   - AES-256 for symmetric encryption
   - RSA-2048 for asymmetric encryption
   - Secure key generation and storage

2. **Authentication:**
   - Password hashing using SHA-256
   - Session-based user management
   - Role-based access control

### Database Schema

```sql
users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    password_hash VARCHAR(255),
    group_name ENUM('H', 'R')
)

healthcare (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender BOOLEAN,
    age INT,
    weight FLOAT,
    height FLOAT,
    health_history VARCHAR(255),
    encrypted_ssn BLOB
)
```

## Expected Results

### Healthcare Providers (Group H):
- Full CRUD access to patient records
- Ability to view and edit all patient information
- Access to encrypted SSN data

### Researchers (Group R):
- Read-only access to non-sensitive data
- Access limited to demographic and health metrics
- No access to personal identifiers or SSN

## Methodology

1. **Security First Approach:**
   - Encryption at rest for sensitive data
   - Role-based access control
   - Secure session management

2. **Data Privacy:**
   - Differentiated access levels
   - Encrypted storage of sensitive information
   - Minimal data exposure principle

3. **User Experience:**
   - Simple and intuitive interface
   - Clear access level indicators
   - Efficient data management workflows

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ajaychary06/Projects/blob/main/LICENSE) file for details.


## Contact

Your Name - [Ajaychary Kandukuri](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a) - ajaycharykandukuri0629@gmail.com
