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

def get_figure_dimensions(fw_pixels, fh_pixels):
    myfigure_dpi = 100
    figure_width = fw_pixels/float( myfigure_dpi )
    figure_height = fh_pixels/float( myfigure_dpi )
    return figure_width, figure_height, myfigure_dpi

def set_fig_elements_size():
    plt.rcParams['axes.labelsize'] = 15
    plt.rcParams['axes.titlesize'] = 15
    plt.rcParams['figure.titlesize'] = 20

def fig_init(axs_rows, axs_cols, share_x_axis, share_y_axis, xlabels, ylabels, titles, suptitle_str, fig_num, fig_pos, fig_size):
    if len(fig_size)==0:
        fw,fh,dpi = get_figure_dimensions(1920,1080)
        fig_size = [fw/2,fh]
    set_fig_elements_size()
    if len(xlabels)!=axs_rows*axs_cols or len(ylabels)!=axs_rows*axs_cols or len(titles)!=axs_rows*axs_cols:
        print("Error : mismatch in # of (xlabels/ylabels/titles)") ; exit()
    fig, axs = plt.subplots(nrows=axs_rows, ncols=axs_cols, sharex=share_x_axis, sharey=share_y_axis, num=fig_num, figsize=( fig_size[0], fig_size[1] ), clear=True)
    fig.canvas.manager.window.move(fig_pos,0)
    #
    if axs_rows*axs_cols==1:
        axs.cla()
        axs.grid()
        axs.set_xlabel(xlabels[0])
        axs.set_ylabel(ylabels[0])
        axs.set_title(titles[0], y=1.01,wrap=True)
    elif axs_rows==1:
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
