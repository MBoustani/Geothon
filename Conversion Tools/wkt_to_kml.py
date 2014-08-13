#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/wkt_to_kml.py
Description:   This code converts wkt data format to kml format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

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

#an example of WKT data
wkt_line = "LINESTRING (102 0,103 1,104 0,110 1)"

#convert WKT data to geometry format
line_geometry = ogr.CreateGeometryFromWkt(wkt_line)

#set driver to KML to be able to create kml file
driver = ogr.GetDriverByName('KML')

#output kml file name
kml_file = 'line.kml'

#output kml file layer name
layer_name = 'kml_layer'

#create kml datasource
kml_datasource = driver.CreateDataSource(kml_file)

#create kml layer
kml_layer = kml_datasource.CreateLayer(layer_name, srs, ogr.wkbLineString)

#define a feature
feature = ogr.Feature(kml_layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(line_geometry)

#create feature in layer
kml_layer.CreateFeature(feature)
