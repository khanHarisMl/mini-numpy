class MiniArray:
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __repr__(self):
        return f"MiniArray({self.data})"

    def append(self, value):
        self.data.append(value)
    
    def sum(self):
        i = 0
        sum = 0
        while i < len(self.data):
            sum += self.data[i]
            i += 1
        return sum
    
    def mean(self):
        if len(self.data) == 0:
            print("Error, empty input array, cannot calculate mean")
        i = 0
        sum = 0
        while i < len(self.data):
            sum += self.data[i]
            i += 1
        return sum/i
    
    def min(self):
        if len(self.data) == 0:
            print("Error, empty input array, cannot calculate minimum")
            return None
        i = 1
        curr_min = self.data[0]
        while i < len(self.data):
            if curr_min > self.data[i]:
                curr_min = self.data[i]
            i += 1
        return curr_min

    def max(self):
        if len(self.data) == 0:
            print("Error, empty input array, cannot calculate maximum")
            return None
        i = 1
        curr_max = self.data[0]
        while i < len(self.data):
            if curr_max < self.data[i]:
                curr_max = self.data[i]
            i += 1
        return curr_max
    