def f(start, result, data, angka):
    if start >= len(data):
        return result
    
    if type(data[start]) == int:
        if data[start] != angka:
            return f(start + 1, result + (data[start],), data, angka)
        else:
            return f(start + 1, result, data, angka)
    else:
        x = ff(0, (), data[start], angka)
        return f(start + 1, result + (x,), data, angka)

def ff(start, result, tup, angka):
    if start >= len(tup):
        return result
    if type(tup[start]) == int:
        if tup[start] != angka:
            return ff(start + 1, result + (tup[start],), tup, angka)
        else:
            return ff(start + 1, result, tup, angka)
    else:
        t = f(0, (), tup[start], angka)
        return ff(start + 1, result + (t,), tup, angka)

def hapus(data,angka):
    # tulis jawaban anda hanya di dalam fungsi ini saja
    print(f(0, (), data, angka))
            
# data = (1, 2, 3, (1, 2, 3, (1, 2, 3, (1, 2, 3))))
data = (1, 2, 3, (1, 2, 3, (1, 2, 3)))
hapus(data, 3)


# data = (((3,9),2,3,(2,3),5,6,(7,2),8,9,(10,11)))
# angka = 3

# result = []

# for i in data:
#     if type(i) == tuple:
#         temp = []
#         for j in i:
#             if j == angka:
#                 continue
#             else:
#                 temp.append(j)
#         result.append(tuple(temp))
#     elif i == angka:
#         continue
#     else:
#         result.append(i)

# print(result)