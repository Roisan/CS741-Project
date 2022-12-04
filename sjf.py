def calcWT(proc, wt, n):
    rt = [0] * n
    for i in range(n):
        rt[i] = proc[i][1]
    comp = 0
    curTime = 0
    mnm = 999999
    curJob = 0
    check = False
    while comp != n:
        for j in range(n):
            if process[j][2] <= curTime and 0 < rt[j] < mnm:
                mnm = rt[j]
                curJob = j
                check = True
        if not check:
            curTime += 1
            continue

        rt[curJob] -= 1
        mnm = rt[curJob]
        if mnm == 0:
            mnm = 999999

        if rt[curJob] == 0:
            comp += 1
            check = False
            ft = curTime + 1
            wt[curJob] = ft - proc[curJob][1] - proc[curJob][2]
            if wt[curJob] < 0:
                wt[curJob] = 0

        curTime += 1


def calc_tat(proc, wt, tat, n):
    for i in range(n):
        tat[i] = proc[i][1] + wt[i]


def calcTime(proc, n):
    wt = [0]*n
    tat = [0]*n
    total_tat = 0
    total_wt = 0

    calcWT(proc, wt, n)
    calc_tat(proc, wt, tat, n)
    print("  Pr  BT  AT  WT  TAT")

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(" ", proc[i][0], " ", proc[i][1], " ", proc[i][2], " ", wt[i], " ", tat[i])

    print("Avg waiting time:{} and Avg TAT:{}".format(total_wt/n, total_tat/n))


if __name__ == "__main__":
    process = [[0,50,1],[1,2,1],[2,12,6],[3,22,10],[4,13,0],[5,3,2]]
    no = len(process)
    calcTime(process, no)
