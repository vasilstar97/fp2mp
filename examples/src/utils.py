import json
import uuid

def read_json(file_path : str) -> list | dict | None:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return None
    
def write_json(data : dict, file_path : str):
    with open(file_path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_id(*strings : str) -> str:
    namespace = uuid.NAMESPACE_DNS
    uuid5 = uuid.uuid5(namespace, str.join('/', strings))
    return str(uuid5).replace('-', '')