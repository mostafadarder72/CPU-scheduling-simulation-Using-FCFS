#CPU scheduling simulation Using FCFS
def findWaitingTime(processes, n,bt, wt):
    wt[0] = 0
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]

def findTurnAroundTime (processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def CPU_utilization (processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes Burst time Waiting time Turn around time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i+1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])
    print("Average waiting time = %.5f "%(total_wt / n))
    print("Average turn around time = %.5f "%(total_tat / n))
    print("CPU utilization = %.5f "%((total_tat / (total_wt + total_tat)) * 100))


if __name__ == '__main__':
    n = int(input("Enter number of processes: "))
    burst_time = [0] * n
    for i in range(n):
        burst_time[i] = int(input("Enter burst time for process %d: "%(i+1)))
    CPU_utilization(burst_time, n, burst_time)



