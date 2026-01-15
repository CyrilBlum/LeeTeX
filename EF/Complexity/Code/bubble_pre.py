def A_modifiziert(L):
    n = len(L)
    
    #### Pre-Check ####
    # Prüfe, ob die Liste bereits sortiert ist O(n)
    is_sorted = True
    for i in range(n - 1):
        if L[i] > L[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        return L  # Best-Case: O(n)

    # #### FALLBACK: Originaler Algorithmus A (O(n^2)) ####
    bubble_sort(L)
            
    return L  # Worst-Case: O(n^2)  