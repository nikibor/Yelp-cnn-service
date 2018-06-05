class ClassificationSerializer:

    def __init__(self, data):
        self.data = data
        self.text = ''
        self.token = ''

    def is_valid(self):
        if self.data:
            self.text = self.data[0]
            self.token = self.data[1]
            return self.text != '' and self.token != ''
        return False
