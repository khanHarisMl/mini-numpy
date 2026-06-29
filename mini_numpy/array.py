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
        if self.is_2d():
            print("Error! Append only supports 1D arrays")
            return None
        self.data.append(value)
    
    def sum(self):
        sum = 0
        i = 0
        if self.is_2d():
            row = 0
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    sum += self.data[row][column]
                    column += 1
                row += 1
            return sum
        while i < len(self.data):
            sum += self.data[i]
            i += 1
        return sum
    
    def mean(self):
        if len(self.data) == 0:
            print("Error, empty input array cannot calculate mean")
            return None
        i = 0
        sum = 0
        count = 0
        if self.is_2d():
            row = 0
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    sum += self.data[row][column]
                    count += 1
                    column += 1
                row += 1
            return sum / count
        while i < len(self.data):
            sum += self.data[i]
            i += 1
        return sum / i
    
    def min(self):
        if len(self.data) == 0:
            print("Error, empty input array cannot calculate minimum")
            return None
        i = 1
        row = 0
        if self.is_2d():
            curr_min = self.data[0][0]
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    if self.data[row][column] < curr_min:
                        curr_min = self.data[row][column]
                    column += 1
                row += 1
            return curr_min
        else:
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
        row = 0
        if self.is_2d():
            curr_max = self.data[0][0]
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    if self.data[row][column] > curr_max:
                        curr_max = self.data[row][column]
                    column += 1
                row += 1
            return curr_max 
        else:    
            curr_max = self.data[0]
            while i < len(self.data):
                if curr_max < self.data[i]:
                    curr_max = self.data[i]
                i += 1
            return curr_max
    
    def add(self, other):
        if(len(self.data) == 0):
            print("Error, empty input array cannot add")
            return None
        elif self.is_2d():
            if self.shape() != other.shape():
                print("Error, both matrices must have the same shape")
                return None
            result = MiniArray([
                [0] * len(self.data[0])
                for _ in range(len(self.data))
            ])
            row = 0
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    result.data[row][column] = (
                        self.data[row][column]
                        + other.data[row][column]
                    )
                    column += 1
                row += 1
            return result
        else:
            if len(self.data) != len(other.data):
                print("Error, Arrays are not the same length")
                return None
            i = 0
            result = MiniArray([0] * len(self.data))
            while i < len(self.data):
                result.data[i] = self.data[i] + other.data[i]
                i += 1
            return result

    def subtract(self, other):
        if(len(self.data) == 0):
            print("Error, empty input array cannot subtract")
            return None
        elif self.is_2d():
            if self.shape() != other.shape():
                print("Error, both matrices must have the same shape")
                return None
            result = MiniArray([
                [0] * len(self.data[0])
                for _ in range(len(self.data))
            ])
            row = 0
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    result.data[row][column] = (
                        self.data[row][column]
                        - other.data[row][column]
                    )
                    column += 1
                row += 1
            return result
        else:
            if len(self.data) != len(other.data):
                print("Error, Arrays are not the same length")
                return None
            i = 0
            result = MiniArray([0] * len(self.data))
            while i < len(self.data):
                result.data[i] = self.data[i] - other.data[i]
                i += 1
            return result

    def multiply(self, other):
        if(len(self.data) == 0):
            print("Error, empty input array cannot multiply")
            return None
        elif self.is_2d():
            if self.shape() != other.shape():
                print("Error, both matrices must have the same shape")
                return None
            result = MiniArray([
                [0] * len(self.data[0])
                for _ in range(len(self.data))
            ])
            row = 0
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    result.data[row][column] = (
                        self.data[row][column]
                        * other.data[row][column]
                    )
                    column += 1
                row += 1
            return result
        else:
            if len(self.data) != len(other.data):
                print("Error, Arrays are not the same length")
                return None
            i = 0
            result = MiniArray([0] * len(self.data))
            while i < len(self.data):
                result.data[i] = self.data[i] * other.data[i]
                i += 1
            return result
        
    def divide(self, other):
        if(len(self.data) == 0):
            print("Error, empty input array cannot divide")
            return None
        elif self.is_2d():
            if self.shape() != other.shape():
                print("Error, both matrices must have the same shape")
                return None
            result = MiniArray([
                [0] * len(self.data[0])
                for _ in range(len(self.data))
            ])
            row = 0
            while row < len(self.data):
                column = 0
                while column < len(self.data[row]):
                    if other.data[row][column] == 0:
                        print("Error! Division by 0 is undefiend")
                        return None
                    result.data[row][column] = (
                        self.data[row][column]
                        / other.data[row][column]
                    )
                    column += 1
                row += 1
            return result
        else:
            if len(self.data) != len(other.data):
                print("Error, Arrays are not the same length")
                return None
            i = 0
            result = MiniArray([0] * len(self.data))
            while i < len(self.data):
                if other.data[i] == 0:
                    print("Error! Division by 0 is undefiend")
                    return None
                result.data[i] = self.data[i] / other.data[i]
                i += 1
            return result
    
    def is_2d(self):
        return len(self.data) > 0 and isinstance(self.data[0], list)
    
    def shape(self):
        if not self.is_2d():
            return(len(self.data),)
        rows = len(self.data)
        columns = len(self.data[0])
        return(rows, columns)
