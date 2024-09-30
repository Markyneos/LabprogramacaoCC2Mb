def permutations(lista:list) -> list:
    if len(lista) == 1:
        return [lista]

    first_element = lista[0]
    rest_perms = permutations(lista[1:])

    perms = []
    
    for perm in rest_perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + [first_element] + perm[i:]
            perms.append(new_perm)


    return perms









numbers = [1, 5, 7, 8]
print(permutations(numbers))