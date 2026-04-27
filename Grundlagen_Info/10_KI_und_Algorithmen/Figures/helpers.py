def calc_gini(class_counts):
    """Return the Gini impurity for a dictionary with class counts.

    Parameters
    ----------
    class_counts : dict
    Mapping of class label to count. Only the counts are used.

    Returns
    -------
    float
    Gini impurity value between 0 and 1, where 0 means all samples belong to one class and 1 means a perfectly even distribution of classes.
    """
    total = sum(class_counts.values())
    if total == 0:
        return 0.0  # No samples, so impurity is 0 by definition

    gini = 1.0
    for count in class_counts.values():
        proportion = count / total
        gini -= proportion ** 2

    return gini

print(calc_gini({'A': 10, 'B': 0}))  # Should be 0.0 (pure)
# simple formula of the above to cross check
print(1 - (10/10)**2 - (0/10)**2)  # Should be 0.0 (pure)
print(calc_gini({'A': 5, 'B': 5}))   # Should be 0.5 (impure)
print(calc_gini({'A': 3, 'B': 7}))   # Should be 0.42 (somewhat impure)
print(calc_gini({'A': 0, 'B': 5, 'C': 10}))   # Should be ~0.44
# simple formula of the above to cross check
print(1 - (0/15)**2 - (5/15)**2 - (10/15)**2)  # Should be ~0.44

# custom calculations
print(calc_gini({'A': 2, 'B': 4}))
