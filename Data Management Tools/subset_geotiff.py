#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Raster/subset_geotiff.py
Description:   This code subsets the GeoTIFF with four corner points and exports new GeoTIFF
Author:        Maziyar Boustani (github.com/MBoustani)
'''

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


geo_transform = gtiff_dataset.GetGeoTransform()
#get west-top point of raster
x_origin = geo_transform[0]
y_origin = geo_transform[3]
#get pixel size for both x and y axis
pixel_x_size = geo_transform[1]
pixel_y_size = geo_transform[5]

#calculating boarder of subset
#number 10 and 250 have chosen arbitrarily
#x_min, x_max, y_min and y_max can be
#replaced with lat long info as well
x_min = x_origin + 10*pixel_x_size
y_min = y_origin + 10*pixel_y_size
x_max = x_origin + 250*pixel_x_size
y_max = y_origin + 250*pixel_y_size

#calculate position info of subset in GeoTIFF
x_off = int((x_min - x_origin)/pixel_x_size)
y_off = int((y_max - y_origin)/pixel_y_size)
x_count = int((x_max - x_min)/pixel_x_size) + 1
y_count = int((y_max - y_min)/pixel_y_size) + 1

#get subset of GeoTIFF in array
subset_data = gtiff_band.ReadAsArray(x_off, y_off, x_count, y_count)

#generate subset GeoTIFF
gtiff_format = "GTiff"
subset_gtiff = 'subset_geotiff.tif'
driver = gdal.GetDriverByName(gtiff_format)
subset_datasource = driver.Create(subset_gtiff, x_count, y_count, 1, gdal.GDT_Byte)
subset_datasource.GetRasterBand(1).WriteArray(subset_data)
