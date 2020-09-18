
def refractory(time, gamma):
    wait = []
    for i in range(len(time) - 1):
        wait.append(time[i + 1] - time[i])
    print(min(wait))
    rp = min(wait) * gamma
    new_time = []
    for i in range(len(time)):
        new_time.append(time[i] - rp * i)
    print(new_time)
    return new_time
