import json

array = input()

info = json.loads(array)

n = int(input())
queries = []
for _ in range(n):
    operation = input()
    queries.append(operation)

def contains_index(string: str) -> bool:
    for i in string:
        if i == '[':
            return True
    return False


def find_index(string: str) -> list:
    result = []
    temp_result = ""
    for i in range(len(string)):
        if string[i] == '[':
            i += 1
            while string[i] != ']':
                temp_result = temp_result + string[i]
                i += 1
        if temp_result != "":
            result.append(int(temp_result))
            temp_result = ""
    return result

def find_key_part(string_with_index: str) -> str:
    result = ""
    for i in string_with_index: # i -> char
        if i == '[':
            return result
        else:
            result = result + i


def parse_query(query, info: dict):
    probable_result = info
    splitted_query = query.split('.')
    step_size = len(splitted_query)
    for step in range(step_size):
        if contains_index(splitted_query[step]) and splitted_query[step][0] != "[":
            result_index = find_index(splitted_query[step])
            result_key_part = find_key_part(splitted_query[step])
            try:
                probable_result = probable_result[result_key_part]
                for index in result_index:
                    probable_result = probable_result[index]
            except Exception as e:
                probable_result = "NOT_FOUND"
        elif splitted_query[step][0] == '[':
            result_index = find_index(splitted_query[step])
            try:
                for index in result_index:
                    probable_result = probable_result[index]
            except Exception as e:
                probable_result = "NOT_FOUND"
        else:
            word = splitted_query[step]
            try:
                probable_result = probable_result[word]
            except Exception as e:
                probable_result = "NOT_FOUND"
    return probable_result


operations = [parse_query(q, info) for q in queries]
result = json.dumps(operations, separators = (',', ":"))

for result in operations:
    if isinstance(result, str) and result != "NOT_FOUND":
        print(f'"{result}"')
    elif isinstance(result, (dict, bool)):
        temp_answer = json.dumps(result, separators= (',', ':'))
        print(temp_answer)
    elif result == None:
        print("null")
    else:
        print(result)

# def cout(string: str):
#     printable_range = string[1:len(string)-1]
#     result = ""
#     for char in printable_range:
#         if char == ',':
#             print()
#             result = ""
#             continue
#         else:
#             result = result + char
#     print(result)

# cout(result)