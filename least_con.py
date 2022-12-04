def least(ws, cs, n, w):
    for m in range(n):
        if ws[m] >= w:
            for j in range(m+1, n):
                if ws[j] < w:
                    continue
                if cs[j] < cs[m]:
                    m = j
            if ws[m] < w:
                return -2
            else:
                return m
    return -2


print("Enter the number of servers:")
no = int(input())
w = [0] * no
c = [0] * no

print("Enter the available capacities of each server")
for i in range(no):
    w[i] = int(input())

print("Enter the number of active connections of each server")
for i in range(no):
    c[i] = int(input())

print("Enter the weight of current connection")
weight = int(input())

selected = least(w, c, no, weight)
if selected >= 0:
    print("Server {} is selected".format(selected + 1))
else:
    print("No available server")
