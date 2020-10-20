probs = []
B = []
for i in range(1,8):
    B.append(i+1)
    probs.append(len(B)/7)
print(B)
print(probs)
for i in probs:
    i = int(i)
for i in probs:
    probs.append((1/8)*i)
    print(probs)
