# Module personnel pour creer l'exploitation/posttraitement de JADIM

#===========================================================
#===========================================================

# python librairies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import generic_module
import plot_module
import math

#===========================================================
#===========================================================
def convert_string(mystring, data_type, n_elements):
    nums = mystring.split()
    #print(nums)
    numpy_array = np.zeros((n_elements), dtype=data_type)
    for el in range(len(nums)):
        numpy_array[el] = nums[el]
    return numpy_array
#--------------------------------------------------------------------
def get_data_in_shape(field_string, ni, nj):
    field = np.zeros((ni*nj))
    for iline in range(len(field_string)):
        current_string = field_string[iline]
        elements_nb = len(current_string.split())
        field_local_array = convert_string(current_string, float, elements_nb)
        for i in range(elements_nb):
            field[3*iline+i] = field_local_array[i]
    final_field = np.reshape(field, (ni,nj), order='F')
    return final_field
#
#--------------------------------------------------------------------
def compute_line_number(ni,nj):
    if ni*nj%3==0:
        line_nb = int(ni*nj/3)
    else:
        line_nb = math.ceil(ni*nj/3)
    #print(f"Number of line per field : {line_nb}")
    return line_nb
#
#--------------------------------------------------------------------
def upper_lower_bounds(node_type, ni, nj):
    if node_type == "vertex":
        index_type = 0
    elif node_type == "velocity_u":
        index_type = 1
    elif node_type == "velocity_v":
        index_type = 2
    elif node_type == "pressure":
        index_type = 3
    else:
        generic_module.throw_error_with_function_name()
        print(f">>> node type {node_type} is unknown - end of program")
        exit()
    line_nb = compute_line_number(ni,nj)
    xlb = index_type * 2 * line_nb + 3
    xub = xlb-1 + line_nb
    ylb = xub+1
    yub = ylb-1 + line_nb
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
    dimensions = convert_string(read_data[0], int, 3)
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

