# https://stackoverflow.com/questions/12521525/reading-metadata-with-python
# from PIL import Image
import win32com.client
import re

# im = Image.open("vector.webp").convert("RGB")
# im.save("vector.jpg","jpeg")
# im.show()

###########################################


image_name = "vector.jpg"

results = []
vector_jpg_item = []

# Create a shell and a namespace
sh = win32com.client.gencache.EnsureDispatch('Shell.Application',0)
ns = sh.NameSpace(r'C:\Users\linpa\AppData\Roaming\JetBrains\PyCharmCE2020.1\scratches')

# Iterate through all files int he namespace and find out which one is the file we want
for item in ns.Items():
    if re.search(image_name, item.Path, re.IGNORECASE) is not None:
        results.append(item.Path)
        vector_jpg_item.append(item)

# print(results)

###########################################


# We need to iterate through an empty file (None) to get a list and a number of file properties
list_of_properties = []
number_of_properties = 0
while True:
    property_name = ns.GetDetailsOf(None, number_of_properties)
    if not property_name:
        break
    list_of_properties.append(property_name)
    number_of_properties += 1

# print(list_of_properties)

###########################################


# We use the list of file properties that we got from the previous set of
# #code to get for a real file
list_of_property_values = []

for property_name_index in range(len(list_of_properties)):
    property_value = ns.GetDetailsOf(vector_jpg_item[0], property_name_index)
    list_of_property_values.append(property_value)
    # print(list_of_properties[property_name_index], property_value)

vector_jpg_dict = dict(zip(list_of_properties, list_of_property_values))

print(vector_jpg_dict)

###########################################

