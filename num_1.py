peoples = {"Иванов": 20, "Сидоров": 68, "Петров": 26, "Смирнов": 68}
peoples["Пупкин"] = 15
peoples["Пельмешкин"] = 33
mx_value = max(peoples.values())
mini_value = min(peoples.values())
mid_value = sum(peoples.values()) / len(peoples.values())

print(f"Средний балл = {mid_value}")
print(
    f"Люди с баллом выше среднего: {[key for key, value in peoples.items() if value > mid_value]}"
)
print(
    f"Максимальный балл: {[key for key in peoples if peoples.get(key) == mx_value]}: {mx_value}"
)
print(
    f"Минимальный балл: {[key for key in peoples if peoples.get(key) == mini_value]}: {mini_value}"
)
