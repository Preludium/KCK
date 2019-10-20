import matplotlib
import colorsys
from matplotlib import pyplot as plt
from matplotlib import colors


def main():
    pomap = []
    map = []
    min_val = 0.432528741577922
    max_val = 1.5383204012924698
    with open('dane.txt', 'r') as f:
        w, h, d = f.readline().split()

        for line in f:
            pom = []
            for item in line.split():
                pom.append((float(item) / 100 - min_val) / (max_val - min_val))
            pomap.append(pom)

        for i in pomap:
            pom = []
            for j in i:
                pom.append(get_gradient(j))
            map.append(pom)

    plt.imshow(map)
    plt.show()            


def hsv2rgb(h, s, v):
    return (h, s, v)


def get_gradient(i):
    if (i < 9/32):   # ziel
        h = i * 2.5
        s = 1
        v = 0
    elif (i < 1 / 2): # zolty
        h = 0.2 + i * 1.5
        s = 1
        v = 0 
    else:           # czerwony
        h = 1
        s = 1 - (i - 1/2) * 2 
        v = 0
    return hsv2rgb(h, s, v)

if (__name__ == '__main__'):
    main()