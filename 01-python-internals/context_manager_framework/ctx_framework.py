"""
Context Manager Framework Skeleton
Stage 1 – Python Internals & Data Model
"""

from contextlib import contextmanager


class FileManager:
    """Simple context manager using __enter__/__exit__."""
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        # TODO: handle exceptions gracefully
        return False  # re-raise exceptions


@contextmanager
def db_transaction(connection):
    """Context manager using contextlib for DB transactions."""
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


if __name__ == "__main__":
    # Example 1: file manager
    with FileManager("example.txt", "w") as f:
        f.write("Hello, context managers!")

    # Example 2: database transaction (requires sqlite3 connection)
    import sqlite3
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")

    with db_transaction(conn) as cur:
        cur.execute("INSERT INTO test (name) VALUES (?)", ("Alice",))

    rows = conn.execute("SELECT * FROM test").fetchall()
    print(rows)
