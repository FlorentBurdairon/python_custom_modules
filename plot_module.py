# Module personnel pour creer des figures et plot des courbes

#===========================================================
#===========================================================

# python librairies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

#===========================================================
#===========================================================

def get_figure_dimensions(fw_pixels, fh_pixels):
    myfigure_dpi = 100
    figure_width = fw_pixels/float( myfigure_dpi )
    figure_height = fh_pixels/float( myfigure_dpi )
    #print(figure_width, figure_height, myfigure_dpi)
    return figure_width, figure_height, myfigure_dpi

def set_fig_and_labels_size(fig_size):
    plt.rcParams['axes.labelsize'] = 25
    plt.rcParams['axes.titlesize'] = 15
    plt.rcParams['figure.titlesize'] = 20
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    #
    if fig_size is None or len(fig_size)==0:
        fw,fh,dpi = get_figure_dimensions(1920,1080)
        #fs = min(fw,fh)
        fs = fh * 20./13.
        fig_size = [fs, fh] # [fs/1.333,fs]
    return fig_size

def allocate_label(labels, nrows, ncols):
    if labels is None:
        labels = [""]*nrows*ncols
    else:
        if len(xlabels)!=axs_rows*axs_cols or len(ylabels)!=axs_rows*axs_cols or len(titles)!=axs_rows*axs_cols:
            print("Error : mismatch in # of (xlabels/ylabels/titles)") ; exit()
    return labels

def allocate_fig_num(fig_num):
    fig_num_list = plt.get_fignums()
    if fig_num is None or fig_num in fig_num_list:
        fig_num = len(fig_num_list)
        while fig_num in fig_num_list:
            fig_num+=1
    return fig_num

def fig_init(axs_rows=1, axs_cols=1, share_x_axis=False, share_y_axis=False, xlabels=None, ylabels=None, titles=None, suptitle_str="", fig_num=None, fig_pos=0, fig_size=None):
    #
    xlabels = allocate_label(xlabels, axs_rows, axs_cols)
    ylabels = allocate_label(ylabels, axs_rows, axs_cols)
    titles = allocate_label(titles, axs_rows, axs_cols)
    #
    fig_num = allocate_fig_num(fig_num)
    fig_size = set_fig_and_labels_size(fig_size)
    #
    fig, axs = plt.subplots(nrows=axs_rows, ncols=axs_cols, sharex=share_x_axis, sharey=share_y_axis, num=fig_num, figsize=( fig_size[0], fig_size[1] ), clear=True, constrained_layout=True)
    fig.canvas.manager.window.move(fig_pos,0)
    #
    plt.suptitle(suptitle_str)
    #
    if axs_rows*axs_cols==1:
        axs.cla()
        axs.grid()
        axs.set_xlabel(xlabels[0])
        axs.set_ylabel(ylabels[0])
        if len(titles[0]) > 0:
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
    return fig, axs
