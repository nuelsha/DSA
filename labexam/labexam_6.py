def delete(array, index):
    if index < 0 or index >= len(array):
        print("Invalid index.")
        return array
    return array[:index] + array[index+1:]

print(delete([3, 7, 1, 9, 4, 4 ,6], 6))