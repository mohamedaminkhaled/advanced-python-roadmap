# 🐍 Stage 1: Python Internals & Data Model

## 🎯 Goal
Master the Python data model, descriptors, and metaclasses.  
By the end of this stage I should be able to:
- Build custom classes that behave like Python built-ins.
- Control attribute access with **descriptors**.
- Enforce design rules with **metaclasses**.
- Understand Python internals (GIL, GC, bytecode).

---

## 📂 Projects
1. **Custom ORM** → implement a lightweight ORM using descriptors and metaclasses.  
2. **Config Manager** → build a dict-like configuration system with validation.  
3. **Context Manager Framework** → design reusable context managers (like DB transactions).  

---

## 📚 Resources
- *Fluent Python (2nd Edition)* – Luciano Ramalho  
- [Python Data Model – Official Docs](https://docs.python.org/3/reference/datamodel.html)  
- [CPython Internals – RealPython](https://realpython.com/cpython-internals)  
- PyCon Talk: “The Art of Python Data Model”  

---

## ✅ Progress Checklist
- [ ] Review Python Data Model (dunder methods)  
- [ ] Implement descriptors (`__get__`, `__set__`)  
- [ ] Explore metaclasses (`type`, `__new__`, `__init__`)  
- [ ] Inspect CPython bytecode (`dis` module)  
- [ ] Finish all 3 projects  
