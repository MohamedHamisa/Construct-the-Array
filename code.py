def countArray(n, k, x):
    return (abs((1 - pow(1-k, n-1)) // k) + (pow(-1, n-1) if x == 1 else 0)) % (pow(10, 9) + 7)

