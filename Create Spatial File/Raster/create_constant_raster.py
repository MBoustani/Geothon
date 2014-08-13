#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Raster/create_constant_raster.py
Description:   This code creates a constant value raster.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import gdal
except ImportError:
    from osgeo import gdal

from osgeo import osr

import numpy

#To create a GeoTIFF
file_format = "GTiff"
driver = gdal.GetDriverByName(file_format)

file_name = "new_geotiff.tif"

#set raster width and height
raster_x_size = 100
raster_y_size = 100

#3 bands for RGB
number_of_band = 3
raster_type = gdal.GDT_Byte

#create a raster dataset
raster_dataset = driver.Create(file_name,
                               raster_x_size,
                               raster_y_size,
                               number_of_band,
                               raster_type)

#create 3 zeros numpy array for each band
r_band = numpy.zeros((raster_x_size, raster_y_size), dtype=numpy.uint8)
g_band = numpy.zeros((raster_x_size, raster_y_size), dtype=numpy.uint8)
b_band = numpy.zeros((raster_x_size, raster_y_size), dtype=numpy.uint8)

#fill each numpy with constant value
r_band.fill(128)
g_band.fill(255)
b_band.fill(0)

#add values to 3 raster bands
raster_dataset.GetRasterBand(1).WriteArray(r_band)
raster_dataset.GetRasterBand(2).WriteArray(g_band)
raster_dataset.GetRasterBand(3).WriteArray(b_band)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#left-bottom of raster
xmin = 0
ymin = 0

#pixel size
pixel_size = (.5, .5)

#set raster geotransform
raster_dataset.SetGeoTransform((xmin, pixel_size[0], 0, ymin, 0, pixel_size[1]))

#set raster projection
raster_dataset.SetProjection(srs.ExportToWkt())
