#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_multipoint.py
Description:   This code create points shapefile from latitudes and longitues.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

import os
from netCDF4 import Dataset

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr

#an exmaple of netCDF file
nc_file = "../static_files/netcdf/airs_h2o_128x256_miroc5_sep04.nc"

#open the netCDF file
nc_dataset = Dataset(nc_file, 'r')

#netCDF variables
latitude = 'lat'
longitude = 'lon'
time = 'time'
value = 'H2OMMRLevStd_average'

#get number of time (time dimension)
num_time = len(nc_dataset.dimensions[time])

#get netCDF variable objects
latitudes = nc_dataset.variables[latitude]
longitudes = nc_dataset.variables[longitude]
values = nc_dataset.variables[value]

#get netCDF variable values
lats = latitudes[:]
lons = longitudes[:]
vals = values[:, :, :, :]

#make a list of latitudes and longitudes
latitudes = [int(i) for i in lats]
longitudes = [int(i) for i in lons]

#define multipoint geometry (datapoints)
multipoint = ogr.Geometry(ogr.wkbMultiPoint)

#an output shapefile name
shapefile = 'multipoints.shp'
#an output shapefile layer
layer_name = 'multipoint_layer'

#create ESRI shapefile dirver
driver = ogr.GetDriverByName('ESRI Shapefile')

#create shapefile data_source(file)
if os.path.exists(shapefile):
    driver.DeleteDataSource(shapefile)
data_source = driver.CreateDataSource(shapefile)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#create a shapefile layer
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbPoint)

#make all columns(fields) in layer
for time in range(num_time):
    field_name = ogr.FieldDefn("time_{0}".format(time), ogr.OFTString)
    field_name.SetWidth(50)
    layer.CreateField(field_name)

for lat in range(len(latitudes)):
    for lon in range(len(longitudes)):
        #define a point geometry
        point = ogr.Geometry(ogr.wkbPoint)
        #add point to the geometry
        point.AddPoint(longitudes[lon], latitudes[lat])
        #create a feature
        feature = ogr.Feature(layer.GetLayerDefn())
        #set point geometry to feature
        feature.SetGeometry(point)
        for time in range(num_time):
            #fill the attribute table with netCDF values for each time
            #putting '0' for 'alt' variable to pick first alt
            feature.SetField("time_{0}".format(time
                                               ), str(vals[lon, lat, 0, time]))

        #create feature in layer
        layer.CreateFeature(feature)

        #destroy feature
        feature.Destroy()
