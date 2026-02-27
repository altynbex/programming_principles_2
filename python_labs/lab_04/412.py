import json

old = input()
new = input()

old_info = json.loads(old)
new_info = json.loads(new)

def apply_fetch(old_array, new_array, path = ""):
    differences = []
    keys = set(old_array.keys() | new_array.keys())
    for key in keys:
        if path == "":
            current_path = key
        else:
            current_path = path + "." + key
        if key in new_array and key in old_array:
            if isinstance(old_array[key], dict) and isinstance(new_array[key], dict):
                differences.extend(apply_fetch(old_array[key], new_array[key], current_path))
            elif old_array[key] != new_array[key]:
                old_val = json.dumps(old_array[key], separators = (',', ':'))
                new_val = json.dumps(new_array[key], separators = (',', ':'))
                differences.append(f"{current_path} : {old_val} -> {new_val}")

        elif key not in old_array:
            new_val = json.dumps(new_array[key], separators = (',', ':'))
            differences.append(f"{current_path} : <missing> -> {new_val}")
        elif key not in new_array:
            old_val = json.dumps(old_array[key], separators = (',', ':'))
            differences.append(f"{current_path} : {old_val} -> <missing>")

    return differences

result = apply_fetch(old_info, new_info, "")

if not result:
    print("No differences")
else:
    for line in sorted(result):
        print(line)
# differences_list = []

# def apply_fetch(old_array, new_array, path = ""):
#     differences = 0
#     keys = []
#     if path == "":
#         new_path = path
#     else:
#         new_path = path + "." + key
#     for key in new_array:
#         keys.append(key)
#     for key in old_array:
#         keys.append(key)

#     for key in keys:
#         if key in old_array and key in new_array:
#             if new_array[key] != old_array[key]:
#                 result = (f"{new_path} : {old_array[key]} -> {new_array[key]}")
#                 differences_list.append(result)
#                 old_array[key] = new_array[key]
#                 differences += 1
#         elif key in old_array and key not in new_array:
#             result = (f"{new_path} : {old_array[key]} -> <missing>")
#             differences_list.append(result)
#         elif key in new_array and key not in old_array:
#             result = (f"{new_path} : <missing> -> {new_array[key]}")
#             differences_list.append(result)
#         elif isinstance(old_array[key], dict) and isinstance(new_array[key], dict):
#             apply_fetch(old_array[key], new_array[key], new_path)
    
#     if differences == 0:
#         print("No differences")
# result = apply_fetch(old_info, new_info)
# print(*differences_list, end = "\n")