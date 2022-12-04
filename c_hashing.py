def hash_labels():
    weight = 5
    labels = [0] * (n0 * weight)
    st = "@"
    for i in range(n0 * weight):
        if i % (weight) == 0:
            st = chr(ord(st) + 1)
        lbl = st + str(i % weight)
        labels[i] = abs(hash(lbl))/pow(10, 19) * 360
        print("{} has hash {}".format(lbl, labels[i]))
    return labels


n0 = 3
S = ["187.100.255.255", "123.200.100.100", "192.168.234.0"]
hash_label = hash_labels()
while True:
    count = len(S)
    h = [0] * count
    asgn = [0] * count
    print(len(hash_label))
    for i in range(len(S)):
        index = 0
        h[i] = hash(S[i])
        asgn[i] = abs(h[i])/pow(10, 19) * 360
        mn = 360
        for j in range(len(hash_label)):
            if hash_label[j] - asgn[i] < 0:
                continue
            if hash_label[j] - asgn[i] < mn:
                index = j
                mn = hash_label[j] - asgn[i]
        index = index//5 + 1
        print("Request {} with hash {} assigned to server {}".format(i + 1, asgn[i], index))
    print("Continue?(y/n)")
    inp = input()
    if inp == "y":
        print("Enter IP address of new request")
        temp = input()
        if temp not in S:
            S.append(temp)
        continue
    else:
        break




