import random

# http://claresloggett.github.io/python_workshops/improved_hammingdist.html
# Return the Hamming distance between string1 and string2.
# string1 and string2 should be the same length.
def hamming_distance(string1, string2):
    # Start with a distance of zero, and count up
    distance = 0
    positions_different = []
    # Loop over the indices of the stringa c b e d a
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
            positions_different.append(i)
    # Return the final count of differences
    return {'distance': distance, 'positions_different': positions_different}


def swap(origin_array, target_array, target_position):
    element_in_target_position = target_array[target_position]
    element_to_be_swapped = origin_array[target_position]
    position_of_element_in_origin_array = origin_array.index(element_in_target_position)
    origin_array[target_position] = element_in_target_position
    origin_array[position_of_element_in_origin_array] = element_to_be_swapped
    return origin_array


def walk_to_better_solution(weaker_solution, stronger_solution):
    results = hamming_distance(''.join(weaker_solution), ''.join(stronger_solution))
    number_of_swaps = int(results['distance'] / 2)
    number_of_random_swaps = random.randrange(1, number_of_swaps+1, 1)
    print(f'Quantidade de swaps {number_of_random_swaps}')
    for i in range(number_of_random_swaps):
        different_array = results['positions_different']
        position_to_swap = random.choice(different_array)
        print(f'Posicao trocada {position_to_swap}')
        different_array.remove(position_to_swap)
        weaker_solution = swap(weaker_solution, stronger_solution, position_to_swap)
        print(f'Solução parcial {weaker_solution}')
        results = hamming_distance(''.join(weaker_solution), ''.join(stronger_solution))
    return weaker_solution


print(walk_to_better_solution(weaker_solution=['a', 'c', 'b', 'e', 'd', 'a'],
                              stronger_solution=['a', 'b', 'c', 'd', 'e', 'a']))
print('------------')
print(walk_to_better_solution(weaker_solution=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a'],
                              stronger_solution=['a', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']))

