from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

# Creating collector instance and collecting all the walls from the model

app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

wall_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

# Iterate over wall and collect Volume data

total_volume = 0.0

for wall in wall_collector:
	vol_param = wall.LookupParameter("Volume")
	if vol_param:
		total_volume = total_volume + vol_param.AsDouble()
		
# Now that the results are collected, print the total
print(total_volume)
	
	
	