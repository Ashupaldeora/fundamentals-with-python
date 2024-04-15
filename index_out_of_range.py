def safe_access(arr, index):
    try:
        value = arr[index]
        return value
    except IndexError:
        print("Error: Index out of range")
        return None

# Example usage
my_list = [1, 2, 3, 4, 5]
index = int(input("Enter the index to access: "))
result = safe_access(my_list, index)
if result is not None:
    print("Value at index", index, "is", result)
