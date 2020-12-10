# From: https://pro.arcgis.com/en/pro-app/tool-reference/topographic-production/polygon-to-centerline.htm
# Name: PolygonToCenterline_sample.py
# Description: Select the rivers and produce centerlines

# Import System Modules
import arcpy

# Check Out Extensions
arcpy.CheckOutExtension('Foundation')

# # Setting Local Variables
# in_features = r'C:\data\CTM.gdb\CTM\HydrographySrf'
# out_feature_class = r'C:\data\CTM.gdb\CTM\HydrographyCrvOut'

# Access feature classes
# From: https://pro.arcgis.com/en/pro-app/arcpy/functions/listfeatureclasses.htm
fc = arcpy.ListFeatureClasses()

# Select only the Rivers subtype
inputLyr = arcpy.MakeFeatureLayer_management(fc[0], "inputLyr", "FCSubtype =  100314")

# Execute Polygon To Centerline
arcpy.topographic.PolygonToCenterline(fc[0], fc[1])

# Check In Extensions
arcpy.CheckInExtension("Foundation")