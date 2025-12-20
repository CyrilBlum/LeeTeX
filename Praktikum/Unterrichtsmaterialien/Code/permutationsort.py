import itertools

def permutations_sort(arr):
    # Die Funktion itertools.permutations generiert alle Permutationen des Arrays in lexikographischer Reihenfolge
    alle_permutationen = itertools.permutations(arr)
    
    for perm_tuple in alle_permutationen:
        aktuelle_permutation = list(perm_tuple)
    
        if all(aktuelle_permutation[i] <= aktuelle_permutation[i+1] for i in range(len(aktuelle_permutation) - 1)):
            return aktuelle_permutation
