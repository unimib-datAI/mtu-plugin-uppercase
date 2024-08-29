import os
import json

file_path = f"{os.path.dirname(os.path.realpath(__file__))}/input.json"
file_open = open(file_path, encoding="utf-8")
data: dict[str, list[str]] = json.load(file_open)

new_column = []
for cell in data["original_column"]:
    new_column.append(cell.upper())

with open(f"{os.path.dirname(os.path.realpath(__file__))}/output/transform.json", 'w', encoding="utf-8") as f:
    json.dump({"new_column": new_column}, f)
