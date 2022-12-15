# Generic modules that can be used in different situations

#================================================================================================
#================================================================================================

# python librairies
import os
import inspect
import numpy as np

#================================================================================================
#================================================================================================

def nombre_premier(N, nlim):
    l=[print(f"{n}".rjust(3) + f" est diviseur de {N} : {N}/{n} = {int(N/n)}") for n in range(2,nlim+1) if N/n==int(N/n)]
    if nlim>=N and len(l)==1:
        print(f"=====> {N} est un nombre premier !!!")
    if len(l)==0:
        print(f"{N} n'a pas de diviseur dans l'intervalle recherche")

#def print_colored_arrow_with ( section_number ):
#    print(colored("------> %u) " % section_number, "green"), end='')

def check_if_string_is_an_integer( mystring ):
    try:
        int( mystring )
        return True
    except ValueError:
        return False

def extract_relative_path_from_absolute_path( directory_path, position=-1 ):
    list_of_successive_directories = directory_path.split('/') # split based on the directory separator '/'
    #print(f"{list_of_successive_directories}")
    list_of_successive_directories = list(filter(None, list_of_successive_directories)) # remove empty strings
    #print(f"{list_of_successive_directories}")
    relative_path = list_of_successive_directories[position]
    return relative_path

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

def throw_error_with_function_name():
    print(f"Error in [{inspect.stack()[1][3]}] from file [{inspect.stack()[1][1]}]")

def convert_string_to_numpy_array(mystring):
    nums = mystring.split()
    ni = len(nums)
    numpy_array = np.zeros((ni))
    for i in range(ni):
        numpy_array[i] = float(nums[i])
    return numpy_array

def convertir_en_secondes(heure,minute,seconde):
    return heure*3600 + minute*60 + seconde

def convertir_en_minutes(heure,minute,seconde):
    return heure/60 + minute + seconde/60

def convertir_en_heures(heure,minute,seconde):
    return heure + minute/60 + seconde/3600

def convertir_en_jours(heure,minute,seconde):
    return convertir_en_heures(heure,minute,seconde)/24
