#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion Tools/geotiff_to_shp_point.py
Description:   This code extracts latitude, longitude and value from GeoTIFF and create point shp file.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

import numpy as np
import os

try:
    import gdal
except ImportError:
    from osgeo import gdal

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr

from gdalconst import GA_ReadOnly

#A GeoTIFF example file
gtif_file = "../static_files/geotiff/aso_albedo.tif"

#open the GeoTIFF dataset
gtiff_dataset = gdal.Open(gtif_file, GA_ReadOnly)

#get GeoTIFF first band
gtiff_band = gtiff_dataset.GetRasterBand(1)

#get GeoTIFF transformation
transform = gtiff_dataset.GetGeoTransform()

#top left pixel longitude
x_origin = transform[0]

#top left pixel latitude
y_origin = transform[3]

#pixel x size
pixel_x_size = transform[1]

#pixel y size
pixel_y_size = transform[5]

#get Geotiff width
tif_x_size = gtiff_dataset.RasterXSize

#get Geotiff height
tif_y_size = gtiff_dataset.RasterYSize

#bottom right pixel longitude
x_end = x_origin + (tif_x_size * pixel_x_size)

#bottom right pixel latitude
y_end = y_origin + (tif_y_size * pixel_y_size)

#get all longitudes
longitudes = np.arange(x_origin, x_end, pixel_x_size)

#get all latitudes
latitudes = np.arange(y_origin, y_end, pixel_y_size)

#get all pixel value
data = gtiff_band.ReadAsArray(0, 0, tif_x_size, tif_y_size)


shapefile = 'geotiff_multipoints.shp'
layer_name = 'geotiff_multipoints_layer'

#create ESRI shapefile dirver
driver = ogr.GetDriverByName('ESRI Shapefile')

#create shapefile data_source(file)
if os.path.exists(shapefile):
    driver.DeleteDataSource(shapefile)
data_source = driver.CreateDataSource(shapefile)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84 Zone 11
srs.ImportFromEPSG(32611)

#create shapefile layer as points data with wgs84 as spatial reference
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbPoint)


long_field = ogr.FieldDefn("Longitude", ogr.OFTString)
long_field.SetWidth(24)
layer.CreateField(long_field)

lat_field = ogr.FieldDefn("Latitude", ogr.OFTString)
lat_field.SetWidth(24)
layer.CreateField(lat_field)

value_field = ogr.FieldDefn("Value", ogr.OFTString)
value_field.SetWidth(24)
layer.CreateField(value_field)

for xi, x in enumerate(longitudes):
    for yi, y in enumerate(latitudes):
        value = data[yi-1][xi-1]

        #define a point geometry
        point = ogr.Geometry(ogr.wkbPoint)

        #add point to the geometry
        point.AddPoint(x, y)

        #create a feature
        feature = ogr.Feature(layer.GetLayerDefn())

        #set point geometry to feature
        feature.SetGeometry(point)

        feature.SetField("Longitude", '{0}'.format(x))
        feature.SetField("Latitude", '{0}'.format(y))
        feature.SetField("Value", '{0}'.format(value))

        #create feature in layer
        layer.CreateFeature(feature)

        #destroy feature
        feature.Destroy()
