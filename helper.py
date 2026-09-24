import json

def load_config(path):
    with open(path, "r") as file:
        config = json.load(file)
        return config

# def filter_positions(positions, max_posting_age = 0):
#     return filter(lambda position: position["days_posted"] <= max_posting_age, positions)