#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Data Management Tools/extract_gtif_x_y_value.py
Description:   This code extracts latitude, longitude and value from GeoTIFF and save as CSV file.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

import numpy as np
import csv

try:
    import gdal
except ImportError:
    from osgeo import gdal

from gdalconst import GA_ReadOnly

#A GeoTIFF example file
gtif_file = "../static_files/geotiff/cea.tif"

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

#make a csv file
with open('gtif_x_y_value.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    #write a header
    writer.writerow(['longitude', 'latitude', 'value'])
    #write latitude, longitude and value for each pixel
    for xi, x in enumerate(longitudes):
        for yi, y in enumerate(latitudes):
            value = data[yi-1][xi-1]
            writer.writerow([x, y, value])
