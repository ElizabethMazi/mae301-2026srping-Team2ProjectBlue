import json

def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]
