class ClassificationSerializer:

    def __init__(self, data):
        self.data = data
        self.vector = ''
        self.hashkey = ''

    def is_valid(self):
        if self.data:
            self.vector = self.data['vector']
            self.hashkey = self.data['hashkey']
            return self.vector != '' and self.hashkey != ''
        return False
