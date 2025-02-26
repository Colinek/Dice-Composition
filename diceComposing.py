import random
import numpy as np

# scales
MajorHexatonic = ['C', 'D', 'E', 'F', 'G', 'A']
MinorHexatonic = ['C', 'D', 'Eb', 'F', 'G', 'Bb']
RitsuOnkai = ['C', 'Db', 'Eb', 'F', 'Ab', 'Bb']
RagaKumud = ['C', 'D', 'E', 'G', 'A', 'B']
MixolydianHexatonic = ['C', 'D', 'F', 'G', 'A', 'Bb']
PhrygianHexatonic = ['C', 'Eb', 'F', 'G', 'Ab', 'Bb']

scales = ['MajorHexatonic', 'MinorHexatonic', 'RitsuOnkai', 'RagaKumud', 'MixolydianHexatonic', 'PhrygianHexatonic']

chosenScale = scales[(random.randint(0, 5))]
scale = eval(chosenScale)
print("Scale chosen:",chosenScale)
print(scale)
print() 

# Roll the dice 16 times
composition = [scale[random.randint(0, 5)] for _ in range(16)]

# Convert list to NumPy array
arr = np.array(composition)

print("Original 1D array:")
print(arr)

# Ensure arr has 16 elements before reshaping
if arr.size == 16:
    # Reshape into a 4x4 matrix
    matrix = arr.reshape(4, 4)

    # Reorder rows so that the first row moves to the last, second row to third, etc.
    rearranged_matrix = matrix[[3, 2, 1, 0]]  # Reverse row order

    print("\nFinal Rearranged 4x4 Matrix:")
    print(rearranged_matrix)  # This prints the final 4x4 matrix

else:
    print(f"Error: Expected 16 elements, but got {arr.size}")
