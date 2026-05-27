class MiniArray:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __repr__(self):
        return f"MiniArray({self.data})"
    