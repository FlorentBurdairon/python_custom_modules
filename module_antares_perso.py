# Import packages
import os
import numpy as np
import antares as ant
import matplotlib.pyplot as plt
import time
#
#================================================
def read_input_data(meshpath, solutpath):
    print("Read input data")
    if len(meshpath)>0:
        reader_type = 'hdf_avbp'
        print(" ---> Read the mesh file")
        reader = ant.Reader(reader_type)
        reader['filename'] = meshpath
        reader['shared'] = True # add read data to the shared instant
        # => useful here because the read data are the mesh which should be shared between all instants
        base = reader.read() # create the Base instance that contains the Zones
    else:
        reader_type = 'hdf_antares'
    #
    # Read the solution files
    print(" ---> Read the solution file")
    reader = ant.Reader(reader_type)
    reader['filename'] = solutpath # files where the solutions are stored
    if len(meshpath)>0:
        reader['base'] = base # tell the Base name
        reader.read()
    else:
        base = reader.read()
    return base
#
#================================================
def domain_reduction(base):
    print("Reduce the size of the computational domain")
    clip = ant.Treatment('threshold')
    clip['base'] = base
    clip['variables'] = ['x', 'y', 'z'] #  variables on which the threshold will be applied
    a = 0.35
    x0 = -a ; x1 = a
    y0 = -a ; y1 = a
    z0 = -a ; z1 = a
    clip['threshold'] = [(x0, x1), (y0, y1), (z0, z1)] # boundaries of the intervals for the threshold to apply
    clip_base = clip.execute()
    print(f" ---> # of points on the original base = {base.grid_points:e}")
    print(f" ---> # of points on the reduced base = {clip_base.grid_points:e}")
    return clip_base
#
#================================================
def transversal_cut(base):
    print("Create a transversal cut")
    print(" ---> Define the properties of the cut and apply")
    plane_cut = ant.Treatment('acut') # cut vs acut : w/o using the VTK library (whatever that means?????)
    plane_cut['base'] = base
    plane_cut['type'] = 'plane'
    plane_cut['origin'] = [0., 0., 0.]
    plane_cut['normal'] = [0., 0., 1.]
    cut_base = plane_cut.execute()
    return cut_base
#
#================================================
def azimuthal_average(base):
    print("Compute the azimuthal average")
    print(" ---> Define the properties of the average and apply")
    azimave = ant.Treatment('AzimuthalAverage') # cut vs acut : w/o using the VTK library (whatever that means?????)
    azimave['base'] = base
    azimave['type'] = 'Full' # compute a 360 degrees average
    azimave['origin'] = [0., 0., 0.]
    azimave['axis'] = [1., 0., 0.] # x direction
    azimave['nb_cuts'] = 180 # number of azimuthal slices for averaging
    #azimave['nb_procs'] = 1 # number of processes
    azim_base = azimave.execute()
    return azim_base
#
#================================================
def write_data(base, dirname, solutfile, prefix):
    print("Write the extracted data for visualisation")
    # Define location
    outdir = os.path.join(dirname, "POST")
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    # Write the base in a VTK binary format file to visualize the skin data extracted in Paraview
    writer = ant.Writer('hdf_antares')
    writer['base'] = base # give the base to write
    outfilename = prefix + solutfile[:-3]
    outfilepath = os.path.join(outdir, outfilename)
    writer['filename'] = outfilepath
    print(" ---> Writing to output file", writer['filename'])
    writer.dump() # write the output file
