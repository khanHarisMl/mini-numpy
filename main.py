from mini_numpy.array import MiniArray
# Stage 2 Test Functions
def test_append():
    print("Testing Append: ")
    arr = MiniArray([1,2,3])
    (arr.append(4))
    print(arr)
    print("Expected output: MiniArray([1, 2, 3, 4])")
    
def test_sum():
    print("Testing Sum: ")
    arr = MiniArray([1,2,3])
    print(arr.sum())
    print("Expected output: 6")

def test_mean():
    print("Testing Mean: ")
    arr = MiniArray([1,2,3])
    print(arr.mean())
    print("Expected output: 2")

def test_min():
    print("Testing Minimum: ")
    arr = MiniArray([1,2,3])
    print(arr.min())
    print("Expected output: 1")

def test_max():
    print("Testing Max: ")
    arr = MiniArray([1,2,3])
    print(arr.max())
    print("Expected output: 3")

# Stage 3 Test Functions

def test_add():
    print("Testing Addition: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr.add(arr2))
    print("Expected output: MiniArray([5, 7, 9])")
def test_subtract():
    print("Testing Subtraction: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr2.subtract(arr))
    print("Expected output: MiniArray([3, 3, 3])")
def test_multiply():
    print("Testing Multiplication: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr.multiply(arr2))
    print("Expected output: MiniArray([4, 10, 18]) ")
def test_divide():
    print("Testing Division: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr2.divide(arr))
    print("Expected output: MiniArray([4.0, 2.5, 2.0])")
# Main
test_append()
test_sum()
test_mean()
test_min()
test_max()
test_add()
test_subtract()
test_multiply()
test_divide()