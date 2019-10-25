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
                    dif = 1 - (pomap[i][j-1] - pomap[i][j]) * 7
                pom.append(get_gradient(pomap[i][j], shading, dif))
            map.append(pom)

    plt.imshow(map)
    plt.show()            


def get_gradient(i, shading, dif):
    if (i < 9/32):   # ziel
        r = i * 2.5
        g = 1
        b = 0
        if (shading):
            r = r * dif 
            g = g * dif
    elif (i < 1 / 2): # zolty
        r = 0.2 + i * 1.5
        g = 1
        b = 0 
        if (shading):
            r = r * dif
            g = g * dif
    else:           # czerwony
        r = 1
        g = 1 - (i - 1/2) * 2 
        b = 0
        if (shading):
            r = r * dif
            g = g * dif
    return (r, g, b)


if (__name__ == '__main__'):
    main()