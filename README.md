# student-management-system
A comprehensive desktop application for managing student records built with Python and Tkinter. The system features a secure login interface and a full-featured student management dashboard with database integration.

## Features
## 🔐 Authentication System
- Secure login interface with username and password validation
- Background image and custom styling
- Input validation for empty fields

## 📊 Student Management
- Add Students: Complete student information entry including roll number, name, contact details, address, gender, and date of birth
- Search Students: Flexible search across all student fields
- Update Records: Modify existing student information
- Delete Students: Remove student records from the system
- View All Students: Display complete student database in a table format
- Export Data: Export student records to CSV format
  
## 💾 Database Integration
- MySQL database connectivity
- Automatic database and table creation
- Secure connection configuration
- Data persistence and integrity

## 🎨 User Interface
- Modern themed interface using ttkthemes
- Real-time clock and date display
- Animated sliding header
- Responsive design with scrollable tables
- Intuitive button layout and navigation

## Prerequisites:
Before running this application, ensure you have the following installed:
- Python 3.7+
- MySQL Server
- Required Python packages (install via pip):
- pip install tkinter
- pip install Pillow
- pip install pymysql
- pip install pandas
- pip install ttkthemes

## Installation
1.Clone or download the project files \ 
2.Ensure all image files are in the project directory:
- bg.jpg - Login background
- logo.png - Application logo
- user.png - Username icon
- password.png - Password icon
- clg.png - College logo \ 
3.The project consists of two main files:
- login.py - Authentication system
- srm.py - Student record management system

## Database Configuration
1.Click "Connect database" in the main application \
2.Enter your MySQL connection details:
- Host name (usually localhost)
- User name (your MySQL username)
- Password (your MySQL password) \ 
3.The system will automatically create the required database and tables

## Managing Students
- Add Student: Fill in all required fields and click "Add Student"
- Search: Enter any student detail to search across all fields
- Update: Select a student from the table and click "Update Student"
- Delete: Select a student and click "Delete Student"
- Export: Click "Export Student" to save data as CSV
