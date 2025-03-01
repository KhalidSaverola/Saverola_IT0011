A = {'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'c', 'k'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'h', 'k'}

print("Number of elements in A ∪ B:", len(A | B))

print("Number of elements in B - (A ∪ C):", len(B - (A | C)))

print("i. {h, i, j, k}:", A & C)
print("ii. {c, d, f}:", A - B)
print("iii. {b, c, h}:", A & B)
print("iv. {d, f}:", A - C)
print("v. {c}:", A & C)
print("vi. {l, m, o}:", B - A)
