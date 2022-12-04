import copy


def calcTime(p, n):
    tmp = copy.deepcopy(p)
    # print(temp)
    ct = [0] * n
    tat = [0] * n
    wt = [0] * n
    awt = 0
    atat = 0
    for j in range(n):
        mnm = 999
        proc = 0
        print(tmp)
        for i in range(n):
            # print(temp[i][2])
            if tmp[i][2] < mnm:
                mnm = tmp[i][2]
                proc = tmp[i][0]
        print(proc)
        tmp[proc][2] = 999
        if j == 0:
            ct[proc] = p[proc][1]
            prev_ct = ct[proc]
        else:
            ct[proc] = prev_ct + p[proc][1]
            prev_ct = ct[proc]

        tat[proc] = ct[proc] - p[proc][2]
        wt[proc] = tat[proc] - p[proc][1]

        awt += wt[proc]
        atat += tat[proc]

    awt /= n
    atat /= n

    print("  Pr  BT  AT  CT  WT  TAT")

    for i in range(n):
        print(" ", p[i][0], " ", p[i][1], " ", p[i][2], " ", ct[i], " ", wt[i], " ", tat[i])

    print("Avg waiting time:{} and Avg TAT:{}".format(awt, atat))


if __name__ == "__main__":
    # process = [[0,1,3],[1,5,1],[2,2,2],[3,6,4],[4,4,0],[5,3,6]]
    process = [[0,50,1],[1,2,1],[2,12,6],[3,22,10],[4,13,0],[5,3,2]]
    no = len(process)
    calcTime(process, no)

