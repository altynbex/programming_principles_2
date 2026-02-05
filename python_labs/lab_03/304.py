class StringHandler():
    def __init__(self):
        pass
    def get_string(self):
        string_name = input()
        return string_name
    def string_upper(self, string_name):
        return string_name.upper()
    
s1 = StringHandler()
string = s1.get_string()
print(s1.string_upper(string))