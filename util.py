# 获取某个指定通道的脉冲
def get_channel(time, chosen_ch, channels):
    index = [i for i, ch in enumerate(channels) if chosen_ch == ch]
    x = []
    for i in index: x.append(time[i])
    return x


def read_data(file):
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    time = []
    channels = []
    for line in lines:
        split = line.strip().split(" ")
        if len(split) != 2:
            continue
        time.append(float(split[0]))
        channels.append(int(split[1]))
    return time, channels
