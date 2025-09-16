# 📦 Project: Custom ORM (Stage 1)

## 🎯 Goal
Build a minimal ORM from scratch to understand:
- Attribute management with **descriptors**.
- Automatic table mapping with **metaclasses**.
- Python’s data model integration.

---

## 📝 Description
This project simulates how ORMs like **SQLAlchemy** or **Django ORM** work at a basic level.  
Features:
- Define models with Python classes.
- Map class attributes to database fields.
- Support CRUD operations (SQLite).

---

## 🚀 Tasks
- [ ] Implement a `Field` descriptor (manages attribute access).  
- [ ] Create a `ModelMeta` metaclass (registers models + builds schema).  
- [ ] Write a `BaseModel` with `save()`, `delete()`, `all()`.  
- [ ] Test with a simple `User` model.  

---

## 📚 Resources
- Fluent Python (Chapter on Descriptors & Metaclasses).  
- SQLAlchemy docs: [https://docs.sqlalchemy.org](https://docs.sqlalchemy.org)  
