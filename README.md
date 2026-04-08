# 🎓 School Management Module

Comprehensive School Management System - Odoo 17 Module

## 📋 Description

A comprehensive module for managing schools using Odoo 17, includes:

- ✅ Student Management
- ✅ Class Management
- ✅ Subject Management
- ✅ Course Management
- ✅ Academic Year Management
- ✅ Student Reports
- ✅ Notifications & Alerts System

## 🚀 Installation

### Requirements
- Odoo 17+
- Python 3.9+

### Installation Steps

1. **Copy the folder to addons:**
```bash
cp -r school /opt/odoo17/odoo17/addons/
```

2. **Add the path to odoo.conf:**
```ini
addons_path = /opt/odoo17/odoo17/addons
```

3. **Restart Odoo and update the Apps list**

4. **Install the module from Apps:**
   - Search for "School"
   - Click Install

## 📁 Project Structure

```
school/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── student.py        # Student Model
│   ├── classs.py         # Class Model
│   ├── subject.py        # Subject Model
│   ├── course.py         # Course Model
│   └── year.py           # Academic Year Model
├── views/
│   ├── base_menu.xml
│   ├── student_view.xml
│   ├── classs_view.xml
│   ├── subject_view.xml
│   ├── course_view.xml
│   └── year_view.xml
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── wizard/
│   ├── __init__.py
│   ├── ex_wizard.py
│   └── ex_wizard_view.xml
├── reports/
│   └── student_report.xml
├── data/
│   └── sequence.xml
├── i18n/
│   ├── school.pot
│   └── ar_001.po
└── static/
    └── description/
        └── icon.png
```

## 🛠️ Key Features

### 1️⃣ Student Management
- Add and edit student information
- Link students to classes and academic years
- Track required documents

### 2️⃣ Class Management
- Create and organize classes
- Assign students to classes
- Manage teachers and supervisors

### 3️⃣ Subject & Course Management
- Create a list of academic subjects
- Link subjects to classes
- Manage training courses

### 4️⃣ Reporting
- Student reports
- Class statistics
- Performance analytics

## 📊 Database

### Main Tables:
- `school.student` - Student data
- `school.class` - Classes
- `school.subject` - Academic subjects
- `school.course` - Courses
- `school.year` - Academic years

## 🔒 Security & Permissions

- ✅ Role-based access control
- ✅ Defined administrative permissions
- ✅ Sensitive data protection

## 🌍 Supported Languages

- 🇸🇦 Arabic
- 🇬🇧 English

## 📝 Important Files

- `__manifest__.py` - Module information
- `models/` - Database models
- `views/` - User interfaces
- `security/` - Security & permissions system

## 🐛 Known Issues

No known issues at this time.

## 💡 Future Features

- [ ] Grades & Exam Management
- [ ] Assignment Submission System
- [ ] Mobile App for Parents & Students
- [ ] Advanced Analytics

## 👨‍💻 Contributors

- Eslam Mohamed Abdelmaqsoud

## 📧 Contact

For questions and suggestions:
- GitHub Issues: https://github.com/EslamMohamedAbdelmaqsoud/school/issues

## 📄 License

MIT License

## 🙏 Thank You

Thank you for using this module! 🎉

---

**Last Updated:** April 8, 2026

