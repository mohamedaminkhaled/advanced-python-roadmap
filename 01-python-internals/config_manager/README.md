# ⚙️ Project: Config Manager (Stage 1)

## 🎯 Goal
Create a configuration manager that behaves like a dictionary but:
- Supports validation.
- Can load/save from JSON or YAML.
- Allows attribute-style access (`config.db.host`).

---

## 📝 Description
The config manager demonstrates:
- `__getitem__`, `__setitem__`, `__getattr__`.
- Validation logic with descriptors.
- Persistence using JSON.

---

## 🚀 Tasks
- [ ] Implement `Config` class with dict-like behavior.  
- [ ] Add validation for specific keys.  
- [ ] Support `.to_json()` and `.from_json()`.  
- [ ] Support attribute access (`config.db_user`).  

---

## 📚 Resources
- Python Data Model (getitem/setitem).  
- `dataclasses` for config structures.  
