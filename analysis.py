import os
import hashlib

def hash(data: str):
    BUFFER_SIZE = 65536
    sha256 = hashlib.sha256()

    sha256.update(data.encode('utf-16'))
    return sha256.hexdigest()

if __name__ == '__main__':
    # Accuracy check
    with open('data.txt', 'r') as file:
        original = file.read()
    original_hash = hash(original)
    with open('extracted_from_task3.txt', 'r') as file:
        reconstructed = file.read()
    reconstructed_hash = hash(reconstructed)
    print(original_hash == reconstructed_hash)

    # File size check
    original_size = os.path.getsize('data.txt')
    compressed_size = os.path.getsize('compressed_by_task3.txt')
    percentage_change = round((original_size - compressed_size) / original_size, 2)
    if percentage_change >= 0:
        print(f'File size reduced by {percentage_change}%')
    else:
        print(f'File size INCREASED by {-percentage_change}%')

# Hashing referenced from https://www.geeksforgeeks.org/sha-in-python/