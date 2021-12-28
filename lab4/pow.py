def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
 
    for i in range(len(degree) - 1, -1, -1):
      r = (r * base ** int(degree[i])) % module
      base = (base ** 2) % module
 
    return r

print(pow_h(3, 4, 17))
#  3 в степени 4, взятое по модулю 17



print(pow_h(56424, 345, 12348))