class StringOperations:

    def __init__(self, text):
        self.text = text

    def reverse_string(self):
        result = ""

        for char in self.text:
            result = char + result

        return result