#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Raster/geotiff_info.py
Description:   This code reprojects GeoTIFF's projection.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import gdal
except ImportError:
    from osgeo import gdal

from gdalconst import GA_ReadOnly

try:
    import osr
except ImportError:
    from osgeo import osr

#input GeoTIFF example file
in_gtif_file = "../static_files/geotiff/cea.tif"

#open the GeoTIFF dataset
in_gtif_dataset = gdal.Open(in_gtif_file, GA_ReadOnly)

#get input Geotiff width
in_gtif_x_size = in_gtif_dataset.RasterXSize

#get input Geotiff height
in_gtif_y_size = in_gtif_dataset.RasterYSize

#get input Geotiff band
in_gtif_band = in_gtif_dataset.GetRasterBand(1)

#get raster band type
in_band_type = in_gtif_band.DataType

#get geotiff driver by name
in_gtif_driver = in_gtif_dataset.GetDriver()

#get input GeoTIFF data
data = in_gtif_band.ReadAsArray(0, 0, in_gtif_x_size, in_gtif_y_size)


#output GeoTIFF file name
out_gtif_file = 're_projected_geotiff.tif'

#create spatial reference
srs = osr.SpatialReference()
#in this case WGS84
srs.ImportFromEPSG(4326)

#create an output GeoTIFF
out_gtif_dataset = in_gtif_driver.Create(out_gtif_file,
                               in_gtif_x_size,
                               in_gtif_y_size,
                               1,
                               in_band_type)

#add data from input GeoTIFF
out_gtif_dataset.GetRasterBand(1).WriteArray(data)

#reptoject output GeoTIFF
out_gtif_dataset.SetProjection(srs.ExportToWkt())
