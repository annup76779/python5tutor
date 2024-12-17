def levenshtein_distance_memo(s1, s2, memo=None):
    # Initialize memo dictionary on the first call
    if memo is None:
        memo = {}

    # Check if the result is already in the memo
    if (len(s1), len(s2)) in memo:
        return memo[(len(s1), len(s2))]

    # Base cases
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # If last characters are the same, no cost to edit
    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    # Recursively compute the distances, but check the memo first
    dist_insert = levenshtein_distance_memo(s1, s2[:-1], memo) + 1
    dist_delete = levenshtein_distance_memo(s1[:-1], s2, memo) + 1
    dist_substitute = levenshtein_distance_memo(s1[:-1], s2[:-1], memo) + cost

    # Find the minimum of the three distances
    min_dist = min(dist_insert, dist_delete, dist_substitute)

    # Store the result in the memo before returning
    memo[(len(s1), len(s2))] = min_dist
    return min_dist

str1 = "k2157946"
str2 = "KU13043"

distance = levenshtein_distance_memo(str1, str2)
print(distance)
