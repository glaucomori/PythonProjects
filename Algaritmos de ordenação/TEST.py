import random
from sorting import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort

random_list = random.sample(range(1,1000), 25)

sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

inverted_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

repeated_list = [3, 3, 3, 2, 2, 4 ,3, 1, 4, 0]

lista = random_list

if __name__ == "__main__":
    print('\nLista original')
    print(lista)

    # selection_sort(lista)
    # bubble_sort(lista)
    # insertion_sort(lista)
    merge_sort(lista)
    # quick_sort(lista)

    print('\nLista ordenada:')
    print(lista)