class ClassificationSerializer:

    def __init__(self, data):
        self.data = data
        self.vector = ''

    def is_valid(self):
        if self.data:
            self.vector = self.data['vector']
            return self.vector != '' or self.vector != None
        return False
