#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Raster/geotiff_info.py
Description:   This code gives geotiff information.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import gdal
except ImportError:
    from osgeo import gdal
from gdalconst import GA_ReadOnly

#GeoTIFF example file
gtif_file = "../static_files/geotiff/cea.tif"

#open the GeoTIFF dataset
gtif_dataset = gdal.Open(gtif_file, GA_ReadOnly)

#get geotiff file name
gtif_name = gtif_dataset.GetDescription()

#get geotiff driver by name
gtif_driver = gtif_dataset.GetDriver().LongName

#get geotiff metadata
gtif_metadata = gtif_dataset.GetMetadata_Dict()

#get geotiff projection
gtif_prj = gtif_dataset.GetProjection()

#get geotiff geographic transformation
gtif_geo_trans = gtif_dataset.GetGeoTransform()

#get geotiff origin from transformation
gtif_origin = (gtif_geo_trans[0], gtif_geo_trans[3])

#get geotiff pixel size from transformation
gtif_pixel_size = (gtif_geo_trans[1], gtif_geo_trans[5])

#get geotiff width
gtif_x_size = gtif_dataset.RasterXSize

#get geotiff height
gtif_y_size = gtif_dataset.RasterYSize

#get geotiff number of bands
gtif_num_band = gtif_dataset.RasterCount


for i in range(gtif_num_band):
    #get raster band
    band = gtif_dataset.GetRasterBand(i + 1)
    #get raster band type
    band_type = gdal.GetDataTypeName(band.DataType)
    #get raster min pixel value
    band_min = band.GetMinimum()
    #get raster max pixel value
    band_max = band.GetMaximum()
    if band_min == None and band_max == None:
        band_min, band_max = band.ComputeRasterMinMax(i + 1)
    #get raster color table if it has
    color_table = band.GetRasterColorTable()
    #get number of overviews in raster
    num_overview = band.GetOverviewCount()
    #get raster block size
    block_size = band.GetBlockSize()
    #get raster NoDataValue
    nodata_value = band.GetNoDataValue()
    #get raster statistics, like mean and std pixel values
    stats = band.GetStatistics(True, True)

#print geotiff information
print "File Name: {0}".format(gtif_name)
print "Driver Name: {0}".format(gtif_driver)
print "Metadata: {0}".format(gtif_metadata)
print "Projection: {0}".format(gtif_prj)
print "Origin: {0}".format(gtif_origin)
print "Pixel Size: {0}".format(gtif_pixel_size)
print "Width(X): {0}".format(gtif_x_size)
print "Height(Y): {0}".format(gtif_y_size)
print "Number of Bands: {0}".format(gtif_num_band)
print "     Band Type: {0}".format(band_type)
print "     Band Min: {0}".format(band_min)
print "     Band Max: {0}".format(band_max)
print "     Band Mean: {0}".format(stats[2])
print "     Band Std: {0}".format(stats[3])
print "     Block Size: {0}".format(block_size)
print "     Color Table: {0}".format(color_table)
print "     Number of Overview: {0}".format(num_overview)
print "     NoData Value: {0}".format(nodata_value)

