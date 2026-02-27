import json

source = input()
patch = input()


source_info = json.loads(source)
patch_info = json.loads(patch)

def apply_fetch(source, patch):
    for key in patch:
        if patch[key] is None:
            if key in source:
                del source[key]
        elif key in source and isinstance(source[key], dict) and isinstance(patch[key], dict):
            apply_fetch(source[key], patch[key])
        else:
            source[key] = patch[key]
    return source

result = apply_fetch(source_info, patch_info)

print(json.dumps(result, separators = (',', ':'), sort_keys = True))