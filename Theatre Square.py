def flagStones(n, m, a):
    if n // a == n / a:
        x = n / a
    else:
        x = (n // a) + 1
    
    if m // a == m / a:
        y = m / a
    else:
        y = (m // a) + 1
    
    return int(x*y)
 
 
u = input()
n, m, a = u.split()
no_of_fStones = flagStones(int(n), int(m), int(a))
print(no_of_fStones)
