import matplotlib.pyplot as plt

def time_from_str(s):
    m, s = s.split(':')
    return int(m)+int(s)/60

# x and y are the index in data
def print_plot(x, y):
    plt.plot(data[x], data[y])
    plt.locator_params(axis='x', nbins=6)
    plt.xlabel(labels[x])
    plt.locator_params(axis='y', nbins=6)
    plt.ylabel(labels[y])
    plt.show()

labels = ['Time(min)', 'P(hPa)', 'T(°C)', 'U(%)', 'Wsp(m/s)', 'Wdir(°)',
          'Lon(°)', 'Lat(°)', 'Altitude(m)', 'Dew(°C)', 'Vi Te(°C)', 'Rs(m/min)']

file = open('example.txt', 'r')
# [1:-1] because there was a ---- for some reason
# changing to [1:] would be ok
data = file.read().splitlines()[1:-1]
data = [d.split() for d in data]
data = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
data[0] = list(map(time_from_str, data[0]))
for i in range(1, len(data)):
    for j in range(len(data[0])):
        data[i][j] = float(data[i][j])
print_plot(0, 1)
