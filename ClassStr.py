class reverse:

    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


user_input = input("Enter a word: ")
obj = reverse(user_input)
print(obj.reverse_string())
