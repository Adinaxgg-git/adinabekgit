import json
import os

# Пути к файлам
LEADERBOARD_FILE = "leaderboard.json"
SETTINGS_FILE = "settings.json"

def load_json(filename, default):
    if not os.path.exists(filename):
        return default
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Функции для Лидерборда
def get_leaderboard():
    return load_json(LEADERBOARD_FILE, [])

def save_score(name, score, distance):
    data = get_leaderboard()
    data.append({"name": name, "score": score, "distance": int(distance)})
    # Сортируем по очкам (по убыванию) и берем топ 10
    data = sorted(data, key=lambda x: x['score'], reverse=True)[:10]
    save_json(LEADERBOARD_FILE, data)

# Функции для Настроек
def get_settings():
    default = {"sound": True, "car_color": "Red", "difficulty": "Medium"}
    return load_json(SETTINGS_FILE, default)

def save_settings(settings):
    save_json(SETTINGS_FILE, settings)