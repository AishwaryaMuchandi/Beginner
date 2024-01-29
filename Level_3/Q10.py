def customers_without_computer(N, S):
    occupied = set()
    walked_away = 0
    
    for i in range(len(S)):
        customer = S[i]
        if i % 2 == 0:  # Customer arrival
            if len(occupied) < N:
                occupied.add(customer)
            else:
                walked_away += 1
        else:  # Customer departure
            occupied.remove(customer)
    
    return walked_away

# Test Example 1
N1 = 3
S1 = "GACCBDDBAGEE"
print("Output for Example 1:", customers_without_computer(N1, S1))

# Test Example 2
N2 = 1
S2 = "ABCBAC"
print("Output for Example 2:", customers_without_computer(N2, S2))
