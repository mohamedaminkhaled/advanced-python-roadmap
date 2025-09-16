# 🔄 Project: Context Manager Framework (Stage 1)

## 🎯 Goal
Learn context managers deeply by building a reusable framework.  
Use cases:
- Database transactions.
- File operations.
- Resource cleanup.

---

## 📝 Description
The framework will:
- Implement both `__enter__` / `__exit__` and `contextlib.contextmanager`.
- Support nested context managers.
- Provide error handling & rollback (for DB example).

---

## 🚀 Tasks
- [ ] Write a simple context manager with `__enter__` / `__exit__`.  
- [ ] Re-implement using `contextlib.contextmanager`.  
- [ ] Extend to support multiple resources (stacked contexts).  
- [ ] Example: DBTransaction with commit/rollback.  

---

## 📚 Resources
- [contextlib docs](https://docs.python.org/3/library/contextlib.html)  
- Fluent Python – Chapter on Context Managers  
