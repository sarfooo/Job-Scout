import json

def load_config(path):
    with open(path, path) as file:
        config = json.load(file)
        return config

# Other helper functions