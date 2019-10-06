#!/usr/bin/env python3

# TODO
#  1) druga oś x u góry
#  2) boxplot

import matplotlib.pyplot as plt
import pandas as pd

files = {'cel.csv': 's', 'rsel.csv': 'o', 'cel-rs.csv': 'v', '2cel.csv': 'd', '2cel-rs.csv': 'D'}


def main():

    for key, value in files.items():
        df = pd.read_csv(key)
        del df['generation']
        x_axis = (df['effort']/1000).tolist()
        del df['effort']
        mean = (df.mean(axis=1)*100).tolist()
        plt.plot(x_axis, mean, label=key, marker=value, markevery=25)

    plt.xlim(0, 500)
    plt.ylim(60, 100)
    plt.grid(linestyle='-', linewidth=0.5)
    plt.ylabel("Odsetek wygranych gier [%]")
    plt.xlabel("Rozegranych gier (x 1000)")
    plt.title("Wykres")
    plt.legend()
    plt.show()

    
if __name__ == '__main__':
    main()
