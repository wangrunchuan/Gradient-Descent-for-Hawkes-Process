
def read_data(file):
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    time = []
    channels = []
    for line in lines:
        split = line.strip().split(" ")
        time.append(float(split[0]))
        channels.append(int(split[1]))
    return time, channels
