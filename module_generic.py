# Generic modules that can be used in different situations

#================================================================================================
#================================================================================================

# python librairies
import os
import inspect
import numpy as np
import sys
import csv

#================================================================================================
#================================================================================================
#
#================================================
def gather_path(path_elements, checkpath):
    outpath = ''
    for element in path_elements:
        outpath = os.path.join(element)
    if checkpath:
        isdir = os.path.isdir(checkpath)
        isfile = os.path.isfile(checkpath)
        if not(isfile or isdir):
            print(f"WARNING: can't find {checkpath}! Ending now...") ; exit()
    return outpath
#
#================================================
def check_ispath(checkpath):
    isdir = os.path.isdir(checkpath)
    isfile = os.path.isfile(checkpath)
    if not(isfile or isdir):
        print(f"WARNING: can't find {checkpath}! Ending now...") ; exit()
#
#================================================
def nombre_premier(N, nlim):
    l=[print(f"{n}".rjust(3) + f" est diviseur de {N} : {N}/{n} = {int(N/n)}") for n in range(2,nlim+1) if N/n==int(N/n)]
    if nlim>=N and len(l)==1:
        print(f"=====> {N} est un nombre premier !!!")
    if len(l)==0:
        print(f"{N} n'a pas de diviseur dans l'intervalle recherche")
#
#================================================
#def print_colored_arrow_with ( section_number ):
#    print(colored("------> %u) " % section_number, "green"), end='')
#
#================================================
def check_if_string_is_an_integer( mystring ):
    try:
        int( mystring )
        return True
    except ValueError:
        return False
#
#================================================
def extract_relative_path_from_absolute_path( directory_path, position=-1 ):
    list_of_successive_directories = directory_path.split('/') # split based on the directory separator '/'
    #print(f"{list_of_successive_directories}")
    list_of_successive_directories = list(filter(None, list_of_successive_directories)) # remove empty strings
    #print(f"{list_of_successive_directories}")
    relative_path = list_of_successive_directories[position]
    return relative_path
#
#================================================
def get_dat_files_from_directory_and_sort_them ( mydirectory ):
    mylist_of_files = os.listdir ( mydirectory )
    mylist_of_dat_files = list()
    for current_file in mylist_of_files:
        if ".dat" in current_file:
            if check_if_string_is_an_integer( current_file[-5] ): # there could be dat files whose names end with "scalar_field.dat" that we dont want
                mylist_of_dat_files.append( current_file )
#    print( mylist_of_dat_files )
    mylist_of_dat_files.sort()
    return mylist_of_dat_files
#
#================================================
def throw_error_with_function_name():
    print(f"Error in [{inspect.stack()[1][3]}] from file [{inspect.stack()[1][1]}]")
#
#================================================
def convert_string_to_numpy_array(mystring):
    nums = mystring.split()
    ni = len(nums)
    numpy_array = np.zeros((ni))
    for i in range(ni):
        numpy_array[i] = float(nums[i])
    return numpy_array
#
#================================================
def convertir_en_secondes(heure,minute,seconde):
    return heure*3600 + minute*60 + seconde
#
#================================================
def convertir_en_minutes(heure,minute,seconde):
    return heure/60 + minute + seconde/60
#
#================================================
def convertir_en_heures(heure,minute,seconde):
    return heure + minute/60 + seconde/3600
#
#================================================
def convertir_en_jours(heure,minute,seconde):
    return convertir_en_heures(heure,minute,seconde)/24
#
#================================================
def human_readable_time(secondes):
    h = int(secondes/3600)
    m = int((secondes-h*3600)/60)
    s = int(secondes - h*3600 - m*60)
    print(f"{secondes:.0f} s = {h}h {m}min {s}s")
    return [h,m,s]
#
#================================================
def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices
#
#================================================
def progressbar(n,nmax):
    nbin = 100 / nmax
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write(f"[%-100s] %d%%" % ('='*int(nbin*n), nbin*n))
    sys.stdout.flush()
    if n==nmax: print()
    #sleep(0.01)
#
#================================================
def read_data(dirname, filename, delimiter, head='', tail=''):
    filepath = os.path.join(dirname, filename)
    with open(filepath) as file:
        reader = csv.reader(file, delimiter=delimiter)
        rows = []
        for row in reader:
            cleanrow = []
            for l in row:
                if len(l)>0:
                    cleanrow.append(l)
            if len(cleanrow)>0:
                rows.append(cleanrow)
    return rows
#
#================================================
def string_list2numpy_array(list_array):
    N_elems = len(list_array)
    np_array = np.zeros(N_elems)
    for n in range(N_elems):
        element = list_array[n]
        try:
            np_array[n] = float(element)
        except ValueError:
            print(f"ERROR: can't parse element {element}")
    return np_array
