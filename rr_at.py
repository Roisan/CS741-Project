def calcWT(proc, wt, n, q):
    rt = [0] * n
    for i in range(n):
        rt[i] = proc[i][1]
    curTime = 0
    included = [False] * n
    comp = 0
    queue = []

    while comp != n:
        for i in range(n):
            # initial check for available function
            if proc[i][2] <= curTime and rt[i] > 0 and not included[i]:
                queue.append(i)
                included[i] = True
                print("Queue1,", queue)
        if len(queue) == 0:
            check = False
        else:
            check = True
        if not check:
            # print("Test")
            curTime += 1
            continue
        for i in queue:
            if rt[i] > 0:
                if rt[i] > q:
                    print("Process", proc[i][0], " is executed")
                    rt[i] -= q
                    curTime += q
                    p = queue.pop(0)
                    app = True
                    break
                    # print("pop", p, queue)
                else:
                    curTime += rt[i]
                    print("Process", proc[i][0], " exits at time ", curTime)
                    wt[i] = curTime - proc[i][1] - proc[i][2]
                    rt[i] = 0
                    comp += 1
                    queue.remove(i)
                    app = False
                    break
        # check again if other functions have arrived during execution of chosen function
        for i in range(n):
            if proc[i][2] <= curTime and rt[i] > 0 and not included[i]:
                queue.append(i)
                included[i] = True
        # check if incomplete function exists
        if app:
            queue.append(p)
        print("Queue2,", queue)


def calc_tat(proc, wt, tat, n):
    for i in range(n):
        tat[i] = proc[i][1] + wt[i]


def calcTime(proc, n, q):
    wt = [0] * n
    tat = [0] * n
    total_tat = 0
    total_wt = 0

    calcWT(proc, wt, n, q)
    calc_tat(proc, wt, tat, n)

    print("  Pr  BT  AT  WT  TAT")

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(" ",proc[i][0]," ",proc[i][1]," ",proc[i][2]," ",wt[i]," ",tat[i])

    print("Avg waiting time:{} and Avg TAT:{}".format(total_wt/n,total_tat/n))


if __name__ == "__main__":
    # process = [[0,4,0],[1,5,1],[2,2,2],[3,1,3],[4,6,4],[5,3,6]]
    process = [[0,50,1],[1,2,1],[2,12,6],[3,22,10],[4,13,0],[5,3,2]]
    no = len(process)
    quantum = 2
    calcTime(process, no, quantum)
