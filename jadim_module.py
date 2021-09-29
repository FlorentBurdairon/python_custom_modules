# Module personnel pour creer l'exploitation/posttraitement de JADIM

#===========================================================
#===========================================================

# python librairies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from termcolor import colored
import os
import generic_module
import plot_module

#===========================================================
#===========================================================
def convert_string(mystring, data_type):
    nums = mystring.split()
    #print(nums)
    numpy_array = np.zeros((3), dtype=data_type)
    for el in range(len(nums)):
        numpy_array[el] = nums[el]
    return numpy_array
#--------------------------------------------------------------------
def get_data_in_shape(field_string, ni, nj):
    field = np.zeros((ni*nj))
    for el in range(len(field_string)):
        field_local_array = convert_string(field_string[el], float)
        for i in range(3):
            field[3*el+i] = field_local_array[i]
    final_field = np.reshape(field, (nj,ni))
    return final_field
#
#--------------------------------------------------------------------
def upper_lower_bounds(node_type, ni, nj):
    if node_type == "vertex":
        xlb = 3
        xub = int(ni*nj/3)+2
        ylb = int(ni*nj/3)+3
        yub = 2*int(ni*nj/3)+2
    elif node_type == "velocity_u":
        xlb = 2*int(ni*nj/3)+3
        xub = 3*int(ni*nj/3)+2
        ylb = 3*int(ni*nj/3)+3
        yub = 4*int(ni*nj/3)+2
    elif node_type == "velocity_v":
        xlb = 4*int(ni*nj/3)+3
        xub = 5*int(ni*nj/3)+2
        ylb = 5*int(ni*nj/3)+3
        yub = 6*int(ni*nj/3)+2
    elif node_type == "pressure":
        xlb = 6*int(ni*nj/3)+3
        xub = 7*int(ni*nj/3)+2
        ylb = 7*int(ni*nj/3)+3
        yub = 8*int(ni*nj/3)+2
    else:
        generic_module.throw_error_with_function_name()
        print(f">>> node type {node_type} is unknown - end of program")
        exit()
    xlb = xlb-1 ; xub = xub-1 ; ylb = ylb-1 ; yub = yub-1 # substract 1 because of the way python count
    return xlb, xub, ylb, yub
#
#--------------------------------------------------------------------
def check_node_type(node_type):
    print(f"Node type selected : {node_type}")
    list_of_node_types = ["vertex", "velocity_u", "velocity_v", "pressure"]
    if not(node_type in list_of_node_types):
        generic_module.throw_error_with_function_name()
        print(f">>> '{node_type}' is not a valid type of node (list of valid nodes : {[list_of_node_types[i] for i in range(4)]}) - end of program")
        exit()

def read_geom_file(dirname, casename, node_type):
    check_node_type(node_type)
    print(f"Location of the geom file : {dirname}")
    filename = casename + ".geom"
    filepath = dirname + filename
    with open(filepath) as myfile:
        read_data = myfile.readlines()
    #print(read_data[0])
    dimensions = convert_string(read_data[0], int)
    #print(dimensions)
    ni = dimensions[0]
    nj = dimensions[1]
    nk = dimensions[2]
    xlb, xub, ylb, yub = upper_lower_bounds(node_type, ni, nj)
    x_string = read_data[xlb:xub+1]
    coord_x = get_data_in_shape(x_string, ni, nj)
    #print(coord_x[0,:])
    y_string = read_data[ylb:yub+1]
    coord_y = get_data_in_shape(y_string, ni, nj)
    #print(coord_y[:,0])
    return coord_x, coord_y, ni, nj

def plot_geom(coord_x, coord_y, ni, nj, node_type):
    fig, axs = plot_module.fig_init(1,1, False, False, [r'$x$'], [r'$y$'], [f"Node type : {node_type}"], "", 1, 0, [])
    for j in range(nj):
        axs.plot(coord_x[j,:], coord_y[j,:], 'k.-', linewidth=0.5, markerfacecolor='none', markersize=5)
    for i in range(ni):
        axs.plot(coord_x[:,i], coord_y[:,i], 'k.-', linewidth=0.5, markerfacecolor='none', markersize=5)

def read_and_plot_geom(dirname, casename, node_type):
    coord_x, coord_y, ni, nj = read_geom_file(filepath, node_type)
    plot_geom(coord_x, coord_y, ni, nj, node_type)

