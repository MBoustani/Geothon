#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Data Management Tools /netcdf_info.py
Description:   This code gives geotiff information.
Author:        Maziyar Boustani (github.com/MBoustani)
'''
from netCDF4 import Dataset

NETCDF_FILE  =  "../static_files/netcdf/airs_h2o_128x256_miroc5_sep04.nc"

#open a netCDF file
nc_file = Dataset(NETCDF_FILE, mode='r')

#get all variables
all_variables = [variable.encode() for variable in nc_file.variables.keys()]
#list of variables:
#['time', 'time_bnds', 'lon', 'lon_bnds', 'lat', 'lat_bnds', 'alt', 'H2OMMRLevStd_average']


variables = {}
for value in all_variables:
    variable = nc_file.variables[value]
    variables[value] = []
    
    values_attribute = {}
    for att in variable.ncattrs():
        values_attribute[att] = variable.getncattr(att)
    variables[value].append(values_attribute)

    try:
        chunk_cache_information = {}
        for i, each in enumerate(['size','nelems','preemption']):
            chunk_cache_information[each] = variable.get_var_chunk_cache()[i]
        variables[value].append(chunk_cache_information)
    except:
        pass

for each in variables:
    print "Variable: {0}".format(each)
    for att in variables[each]:
        for a in att:
            print '     {0}: {1}'.format(a, att[a])
    