import arcpy
#Set geoprocessing environmnets
arcpy.env.workspace = "C:\EsriTraining\PythonGP10_0\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True
#Create list of feature classes in SanJuan.gdb
fcList = arcpy.ListFeatureClasses()
#Create a loop to buffer Lakes and Streams
bufferList = []
for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", dissolve_option="All")
        bufferList.append(fc + "Buffer")
arcpy.Union_analysis(bufferList, "WaterBuffers")

        
        