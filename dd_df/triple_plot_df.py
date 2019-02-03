import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def triple_plot_df(df, intervals=[[1.0,2.0]], nev_exponent=20, dotsize=5):

    fig, ax = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(6,3), dpi=150)

    ax[0].set_ylabel(r'$\mathrm{n_{e,v}[10^{%2.0d}m^{-3}]}$'%(nev_exponent))
    nev_yval = df['nev']*np.power(10.0,-20)

    clrs_cycle = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5']

    clr = ['k']*len(df['time'])

    ax[0].scatter(df['h98y2'], nev_yval, c='k', s=dotsize, label='')
    ax[1].scatter(df['taue']*1e3, nev_yval, c='k', s=dotsize, label='')
    ax[2].scatter(df['beta'], nev_yval, c='k', s=dotsize, label='')

    for interv, i in zip(intervals, range(len(intervals))):
        msk = (df['time']>=interv[0])&(df['time']<interv[1])
        ax[0].scatter(df['h98y2'][msk], nev_yval[msk], c=clrs_cycle[i], s=dotsize)
        ax[1].scatter(df['taue'][msk]*1e3, nev_yval[msk], c=clrs_cycle[i], s=dotsize,
                      label='[%0.2f,%0.2f]s'%(interv[0],interv[1]))
        ax[2].scatter(df['beta'][msk], nev_yval[msk], c=clrs_cycle[i], s=dotsize, label='')

    ax[0].plot(df['h98y2'], nev_yval, lw=0.2, color='k', ls='--', label='')
    ax[1].plot(df['taue']*1e3, nev_yval, lw=0.2, color='k', ls='--', label='')
    ax[2].plot(df['beta'], nev_yval, lw=0.2, color='k', ls='--', label='')

    ax[0].set_xlabel(r'$\mathrm{H_{98,y2}}$')
    ax[1].set_xlabel(r'$\mathrm{\tau\,[ms]}$')
    ax[2].set_xlabel(r'$\mathrm{\beta_{N}}$')

    plt.tight_layout()
    #plt.show()
    return fig, ax