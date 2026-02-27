import importlib

n = int(input())

def isDotted(module: str) -> bool:
    return "." in module

for i in range(n):
    oper_info = list(map(str, input().split()))
    module = oper_info[0]
    attribute = oper_info[1]
    module_import_status, attribute_implement_status = False, False
    # check whether the module exists
    try:
        importlib.import_module(module)
        module = importlib.import_module(oper_info[0])
        module_import_status = True
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
    if module_import_status == True:
        # now importing the attribute
        valid_attr = getattr(module, attribute) if hasattr(module, attribute) else "ATTRIBUTE_NOT_FOUND"
        if valid_attr != "ATTRIBUTE_NOT_FOUND":
            if callable(valid_attr):
                print("CALLABLE")
            else:
                print("VALUE")
        else:
            print(valid_attr)

# try:
#                 secondary_module = importlib.import_module(attr)
#                 secondary_module_status = True
#             except Exception:
#                 print("CALLABLE")
#             if secondary_module_status == True or isinstance(attr, (int, str, tuple, list, float)):
#                 print("VALUE")