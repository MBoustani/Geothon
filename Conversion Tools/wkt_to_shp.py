#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/wkt_to_shp.py
Description:   This code converts wkt data format to shapefile format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#an example WKT data
wkt_line = "LINESTRING (102 0,103 1,104 0,110 1)"

#convert WKT format to geometry format
line_geometry = ogr.CreateGeometryFromWkt(wkt_line)

#set driver to ESRI shapefile to be able to create shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')

#shapefile file name to generates
shp_file = 'shapefile.shp'
#shapefile layer name to generates
layer_name = 'shapefile_layer'

#create shapefile data_source(file)
if os.path.exists(shp_file):
    driver.DeleteDataSource(shp_file)
shp_datasource = driver.CreateDataSource(shp_file)

#create a shapefile layer
shp_layer = shp_datasource.CreateLayer(layer_name, srs, ogr.wkbLineString)

#define a feature
feature = ogr.Feature(shp_layer.GetLayerDefn())

#set geometry to shapefile feature
feature.SetGeometry(line_geometry)

#create feature in layer
shp_layer.CreateFeature(feature)
