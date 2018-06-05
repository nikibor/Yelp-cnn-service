class ClassificationSerializer:

    def __init__(self, data):
        self.data = data
        self.text = ''
        self.token = ''

    def is_valid(self):
        if self.data:
            self.text = self.data['text']
            self.token = self.data['token']
            return self.text != '' and self.token != ''
        return False
