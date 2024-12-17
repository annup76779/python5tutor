def test(n):
    k = 0
    for i in range(n):
        k += i
    for j in range(n):
        k += j
    # O(2n) -> O(n)
    return k


# order - O(1), O(log), O(n), O(n log n), O(n^2), O(n^2), ...O(n^n), ..

print(test(5))
