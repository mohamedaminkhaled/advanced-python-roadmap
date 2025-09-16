"""
Config Manager Skeleton
Stage 1 – Python Internals & Data Model
"""

import json


class Config(dict):
    """Dictionary-like config manager with attribute access."""

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"No config key: {key}")

    def __setattr__(self, key, value):
        # TODO: add validation here
        self[key] = value

    def to_json(self, path):
        with open(path, "w") as f:
            json.dump(self, f, indent=2)

    @classmethod
    def from_json(cls, path):
        with open(path) as f:
            data = json.load(f)
        return cls(data)


if __name__ == "__main__":
    config = Config(db_host="localhost", db_port=5432)
    print(config.db_host)

    config.to_json("config.json")
    loaded = Config.from_json("config.json")
    print(loaded.db_port)
