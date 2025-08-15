


# A RAY (Funny.) - v1.0.0
# > ItzTen
# 
# This module give some useful function to work on arrays


# Create packs of values in the array
def array_pack(array: list, pack_size: int = 2):
    # Iterates through the length of the list
    # INT Divive the length of the list by the pack size to know the minimal amount of packs

    packed_array = [[] for i in range((len(array)//pack_size) + 1)]

    for i in range(len(array)):
        packed_array[i//pack_size].append(array[i])
    
    if packed_array[len(packed_array) - 1] == []: del packed_array[len(packed_array) - 1]
    
    
    return packed_array


if (__name__ == "__main__"): print(array_pack([1, 2, 3, 4, 5, 6, 7, 8 ,9, 0], 3))    