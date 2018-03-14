import arcpy
arcpy.env.workspace = "C:\EsriTraining\PythonGP10_0\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True
#Create Python list of treatment area feature classes
treatmentList = ["RoadBuffers", "WaterBuffers"]
#Union treatment areas
arcpy.Union_analysis(treatmentList, "NonChemical")
