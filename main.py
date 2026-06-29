from mini_numpy.array import MiniArray
# Stage 2 Test Functions
def test_append():
    print("Testing Append 1D: ")
    arr = MiniArray([1,2,3])
    (arr.append(4))
    print(arr)
    print("Expected output: MiniArray([1, 2, 3, 4])")

    print("Testing Append 2D: ")
    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    matrix.append(5)
    print("Expected output: Error! Append only supports 1D arrays")
    print(matrix)
    print("Expected output: MiniArray([[1, 2], [3, 4]])")

    
def test_sum():
    print("Testing Sum 1D: ")
    arr = MiniArray([1,2,3])
    print(arr.sum())
    print("Expected output: 6")

    print("Testing Sum 2D: ")
    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    print(matrix.sum())
    print("Expected output: 10")

def test_mean():
    print("Testing Mean 1D: ")
    arr = MiniArray([1,2,3])
    print(arr.mean())
    print("Expected output: 2")

    print("Testing Mean 2D: ")
    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    print(matrix.mean())
    print("Expected output: 2.5")


def test_min():
    print("Testing Minimum 1D: ")
    arr = MiniArray([1,2,3])
    print(arr.min())
    print("Expected output: 1")

    print("Testing Minimum 2D: ")
    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    print(matrix.min())
    print("Expected output: 1")

def test_max():
    print("Testing Max 1D: ")
    arr = MiniArray([1,2,3])
    print(arr.max())
    print("Expected output: 3")

    print("Testing Max 2D: ")
    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    print(matrix.max())
    print("Expected output: 4")

# Stage 3 Test Functions

def test_add():
    print("Testing Addition 1D: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr.add(arr2))
    print("Expected output: MiniArray([5, 7, 9])")

    print("Testing Addition 2D: ")
    matrix1 = MiniArray([
        [1,2],
        [3,4]
    ])
    matrix2 = MiniArray([
        [5,6],
        [7,8]
    ])
    print(matrix1.add(matrix2))
    print("Expected output: MiniArray([[6, 8], [10, 12]])")

def test_subtract():
    print("Testing Subtraction 1D: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr2.subtract(arr))
    print("Expected output: MiniArray([3, 3, 3])")

    print("Testing Subtraction 2D: ")
    matrix1 = MiniArray([
        [1,2],
        [3,4]
    ])
    matrix2 = MiniArray([
        [5,6],
        [7,8]
    ])
    print(matrix1.subtract(matrix2))
    print("Expected output: MiniArray([[-4, -4], [-4, -4]])")

def test_multiply():
    print("Testing Multiplication 1D: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr.multiply(arr2))
    print("Expected output: MiniArray([4, 10, 18]) ")

    print("Testing Multiplication 2D: ")
    matrix1 = MiniArray([
        [1,2],
        [3,4]
    ])
    matrix2 = MiniArray([
        [5,6],
        [7,8]
    ])
    print(matrix1.multiply(matrix2))
    print("Expected output: MiniArray([[5, 12], [21, 32]])")


def test_divide():
    print("Testing Division 1D: ")
    arr = MiniArray([1,2,3])
    arr2 = MiniArray([4,5,6])
    print(arr2.divide(arr))
    print("Expected output: MiniArray([4.0, 2.5, 2.0])")
    
    print("Testing Division 2D: ")
    matrix1 = MiniArray([
        [1,2],
        [3,4]
    ])
    matrix2 = MiniArray([
        [5,6],
        [7,8]
    ])
    print(matrix1.divide(matrix2))
    print("Expected output: MiniArray([[0.2, 0.333333], [0.428571, 0.5]])")


# Stage 4 Test Functions

def test_shape():
    print("Testing Shape 1D: ")
    arr = MiniArray([1, 2, 3, 4])
    print(arr.shape())
    print("Expected output: (4,)")

    print("Testing Shape 2D: ")
    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    print(matrix.shape())
    print("Expected output: (2, 2)")

def test_is_2D():
    print("Testing 2D")
    arr = MiniArray([1, 2, 3, 4])
    print(arr.is_2d())
    print("Expected output: False")

    matrix = MiniArray([
        [1,2],
        [3,4]
    ])
    print(matrix.is_2d())
    print("Expected output: True")

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
test_shape()
test_is_2D()