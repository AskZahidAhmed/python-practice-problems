import os

def binary_search_filesystem(directory, target_file):
    files = os.listdir(directory)
    files.sort() 
    low, high = 0, len(files) - 1

    while low <= high:
        mid = (low + high) // 2
        if files[mid] == target_file:
            return os.path.join(directory, target_file)
        elif files[mid] < target_file:
            low = mid + 1
        else:
            high = mid - 1

    return None

# Example usage:
directory_path = "/path/to/your/directory"
target_file_name = "target_file.txt"

result = binary_search_filesystem(directory_path, target_file_name)
if result:
    print("File found:", result)
else:
    print("File not found.")

