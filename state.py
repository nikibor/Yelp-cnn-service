class State:
    def __init__(self, load_embeddings, load_trainables, load_vectors):
        self.load_embeddings = load_embeddings or False
        self.load_trainables = load_trainables or False
        self.load_vectors = load_vectors or False

    def get_current_state(self):
        pass
