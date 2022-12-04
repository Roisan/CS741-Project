# Number of servers
n0 = 5
# Function requests
h = [0] * n0
asgn = [0] * n0
S = ["187.100.255.255", "123.200.100.100", "192.168.234.0"]

while True:
    count = len(S)
    for i in range(count):
        h[i] = hash(S[i])
        print(h[i])
        h[i] = abs(h[i])
        asgn[i] = h[i] % n0
        print("Request {} assigned to server {}".format(i + 1, asgn[i] + 1))
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



