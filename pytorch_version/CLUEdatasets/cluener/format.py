import json

def txt_to_json(txt_file_path, json_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    data = [line.strip() for line in lines]
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# 示例
txt_file_path = 'dev.txt'
json_file_path = 'dev.json'
txt_to_json(txt_file_path, json_file_path)
