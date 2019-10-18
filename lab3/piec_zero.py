from matplotlib import pyplot as plt

def main():
    map = []
    with open('dane.txt', 'r') as f:
        w, h, d = f.readline().split()

        j = 0
        for line in f:
            splitline = line.split()
            pomap = []
            for i in range(len(splitline)):
                pomap[j][i].append(float(splitline[i]))
                pomap[j][i] = get_changed_gradient(pomap[j][i])
            j += 1
            map.append(pomap)
                

    plt.imshow(map)
    plt.show()            

def get_changed_gradient(v):
    if (v < 0.5):
        r = 0
        g = 1
        b = 1 - (v - 0.42) * 7
    else:
        r = (v - 0.56) * 7
        g = 1
        b = 0
    return (r, g, b)

if (__name__ == '__main__'):
    main()