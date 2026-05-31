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
            print("Error, empty input array cannot calculate mean")
        i = 0
        sum = 0
        while i < len(self.data):
            sum += self.data[i]
            i += 1
        return sum/i
    
    def min(self):
        if len(self.data) == 0:
            print("Error, empty input array cannot calculate minimum")
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
            print("Error, empty input array cannot calculate maximum")
            return None
        i = 1
        curr_max = self.data[0]
        while i < len(self.data):
            if curr_max < self.data[i]:
                curr_max = self.data[i]
            i += 1
        return curr_max
    
    def add(self, other):
        sum_arr = MiniArray([0] * len(self.data))
        if (len(self.data) != len(other.data)):
            print("Error, Arrays are not the same length")
            return None
        elif(len(self.data) == 0):
            print("Error, empty input array cannot add")
            return None
        else:
            i = 0
            while i < len(self.data):
                sum_arr.data[i] = self.data[i] + other.data[i]
                i += 1
            return sum_arr

    def subtract(self, other):
        final_arr = MiniArray([0] * len(self.data))
        if(len(self.data) != len(other.data)):
            print("Error, Arrays are not the same length")
            return None
        elif(len(self.data) == 0):
            print("Error! empty input array cannot subtract")
            return None
        else: 
            i = 0
            while i < len(self.data):
                final_arr.data[i] = self.data[i] - other.data[i]
                i += 1
            return final_arr

    def multiply(self, other):
        final_arr = MiniArray([0] * len(self.data))
        if(len(self.data) != len(other.data)):
            print("Error, Arrays are not the same length")
            return None
        elif(len(self.data) == 0):
            print("Error! empty input array cannot multiply")
            return None
        else:
            i = 0
            while i < len(self.data):
                final_arr.data[i] = self.data[i] * other.data[i]
                i += 1
            return final_arr
        
    def divide(self, other):
        final_arr = MiniArray([0] * len(self.data))
        if(len(self.data) != len(other.data)):
            print("Error, Arrays are not the same length")
            return None
        elif(len(self.data) == 0):
            print("Error, empty input array cannot divide")
            return None
        else:
            i = 0
            while i < len(self.data):
                if other.data[i] == 0:
                    print("Error! Division by 0 is undefiend")
                    return None
                final_arr.data[i] = self.data[i] / other.data[i]
                i += 1
            return final_arr
        