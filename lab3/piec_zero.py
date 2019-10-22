from matplotlib import pyplot as plt

map = []

def main():
    pomap = []
    min_val = 0.432528741577922
    max_val = 1.5383204012924698
    with open('dane.txt', 'r') as f:
        w, h, d = f.readline().split()

        for line in f:
            pom = []
            for item in line.split():
                pom.append((float(item) / 100 - min_val) / (max_val - min_val))
            pomap.append(pom)
        dif = 0
        for i in range(len(pomap)):
            pom = []
            for j in range(1,len(pomap[i])):
                shading = False
                if (pomap[i][j-1] > pomap[i][j]):
                    shading = True
                    dif = 1 - (pomap[i][j-1] - pomap[i][j]) * 5
                pom.append(get_gradient(pomap[i][j], shading, dif))
            map.append(pom)

    plt.imshow(map)
    plt.show()            


def hsv2rgb(h, s, v):
    return (h, s, v)


def get_gradient(i, shading, dif):
    if (i < 9/32):   # ziel\
        h = i * 2.5
        s = 1
        v = 0
        if (shading):
            h = h * dif 
            s = s * dif
    elif (i < 1 / 2): # zolty
        h = 0.2 + i * 1.5
        s = 1
        v = 0 
        if (shading):
            h = h * dif
            s = s * dif
    else:           # czerwony
        s = 1 - (i - 1/2) * 2 
        h = 1
        v = 0
        if (shading):
            s = s * dif
            h = h * dif
    return hsv2rgb(h, s, v)


if (__name__ == '__main__'):
    main()