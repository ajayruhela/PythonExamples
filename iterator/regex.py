import re

class RegxDemo:
    def __init__(self,pattern,test_string):
        self.pattern = pattern
        self.test_string = test_string

    def test(self):
        result = re.match(self.pattern, self.test_string)
        if result:
             print("Search successful.")
        else:
             print("Search unsuccessful.")
             



