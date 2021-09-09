# Module personnel pour creer des figures et plot des courbes

#===========================================================
#===========================================================

# python librairies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from termcolor import colored
import os

#===========================================================
#===========================================================

def fig_init(axs_rows, axs_cols, share_x_axis, share_y_axis, xlabels, ylabels, titles, suptitle_str, fig_num, fig_pos):
    if len(xlabels)!=axs_rows*axs_cols or len(ylabels)!=axs_rows*axs_cols or len(titles)!=axs_rows*axs_cols:
        print("Error : mismatch in # of (xlabels/ylabels/titles)") ; exit()
    myfigure_dpi = 100
    fw = 1920.0/float( myfigure_dpi )
    fh = 1080.0/float( myfigure_dpi )
    f_size = min(fw,fh)
    fig, axs = plt.subplots(nrows=axs_rows, ncols=axs_cols, sharex=share_x_axis, sharey=share_y_axis, num=fig_num, figsize=( f_size, f_size ) )
    fig.canvas.manager.window.move(fig_pos,0)
    #
    if axs_rows==1:
        for j in range(axs_cols):
            axs[j].cla()
            axs[j].grid()
            axs[j].set_xlabel(xlabels[j])
            axs[j].set_ylabel(ylabels[j])
            axs[j].set_title(titles[j], y=1.01)
    elif axs_cols==1:
        for i in range(axs_rows):
            axs[i].cla()
            axs[i].grid()
            axs[i].set_xlabel(xlabels[i])
            axs[i].set_ylabel(ylabels[i])
            axs[i].set_title(titles[i], y=1.01)
    else:
        for i in range(axs_rows):
            for j in range(axs_cols):
                axs[i,j].cla()
                axs[i,j].grid()
                axs[i,j].set_xlabel(xlabels[i*axs_cols+j])
                axs[i,j].set_ylabel(ylabels[i*axs_cols+j])
                axs[i,j].set_title(titles[i*axs_cols+j])#, y=1.01)
    plt.suptitle(suptitle_str)
    return fig, axs
