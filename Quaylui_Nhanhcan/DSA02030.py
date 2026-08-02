import itertools 
dauvao = input().split()
c = dauvao[0]
k = int(dauvao[1])
tap = []
for i in range(0,(ord(c) - ord('A'))+1):
    tap.append(chr(65+i))
res = []
for x in itertools.combinations_with_replacement(tap , k):
    res.append("".join(x))
print("\n".join(res))