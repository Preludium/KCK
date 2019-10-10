import matplotlib.pyplot as plt
import pandas as pd

files = {'rsel.csv': 's', 'cel-rs.csv': 'o', '2cel-rs.csv': 'v', 'cel.csv': 'd', '2cel.csv': 'D'}


def main():
    fig, ax = plt.subplots(ncols=2)

    fig.suptitle("Wizualizacja na 5.0 =)")
    avgs = []

    for key, value in files.items():
        df = pd.read_csv(key)
        del df['generation']

        x_axis = (df['effort']/1000).tolist()
        del df['effort']
        avgs.append((df.values[-1] * 100).tolist())
        mean = (df.mean(axis=1)*100).tolist()
        ax[0].plot(x_axis, mean, label=key, marker=value, markevery=25, markeredgecolor='black')

    ax2 = ax[0].twiny()
    ax2.set_xlabel("Pokolenie")
    ax2.set_xlim(0, 200)
    ax2.set_xticks([0, 40, 80, 120, 160, 200])

    ax[1].boxplot(avgs, labels=files.keys(), notch=True, showmeans=True, meanprops=dict(marker='o', markeredgecolor='black', markerfacecolor='blue'))
    ax[1].grid(linestyle='-', linewidth=0.5)
    ax[1].set_ylim(60, 100)
    ax[1].yaxis.tick_right()
    ax[1].set_xticklabels(files.keys(), rotation=45)

    ax[0].set_xlim(0, 500)
    ax[0].set_ylim(60, 100)
    ax[0].grid(linestyle='-', linewidth=0.5)
    ax[0].set_ylabel("Odsetek wygranych gier [%]")
    ax[0].set_xlabel("Rozegranych gier (x 1000)")
    ax[0].legend(loc='lower right', numpoints=2)
    plt.savefig('zad1.pdf')
    plt.show()

    
if __name__ == '__main__':
    main()
