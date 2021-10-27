# Use this to finally create your entire code
# For getting all filenames, properties, exporting it into a CSV file - for Excel
# And it should traverse through directories
# Find out where all the different sources of pictures are from
# And organize them!!!

import win32com.client
import re
# from os import listdir
# from os.path import isfile, join

directory = "C:\\Users\\linpa\\Desktop\\Crap\\iPhone2020\\DCIM\\100APPLE\\"
list_of_items_in_dir = []

# Get all file names of different types in different lists
# We're going to try to do this with win32com as shown below in ns.Items() part
# all_files = [f for f in listdir(directory) if isfile(join(directory, f))]
# jpg_files = [file for file in all_files if file.endswith(".JPG")]
# mov_files = [file for file in all_files if file.endswith(".MOV")]
# mp4_files = [file for file in all_files if file.endswith(".MP4")]
# png_files = [file for file in all_files if file.endswith(".PNG")]

# Create a shell and a namespace
sh = win32com.client.gencache.EnsureDispatch('Shell.Application',0)
ns = sh.NameSpace(r'C:\Users\linpa\Desktop\Crap\iPhone2020\DCIM\100APPLE')

# We need to iterate through an empty file (None) to get a list and a number of file properties
list_of_properties = []
number_of_properties = 0
while True:
    property_name = ns.GetDetailsOf(None, number_of_properties)
    if not property_name:
        break
    list_of_properties.append(property_name)
    number_of_properties += 1

# Iterate through all items and get details
for item in ns.Items():
    list_of_property_values = []
    for property_name_index in range(len(list_of_properties)):
        list_of_property_values.append(ns.GetDetailsOf(item, property_name_index))
    list_of_items_in_dir.append(dict(zip(list_of_properties, list_of_property_values)))
# Now we have a list of all items and their details in the directory

# To get the date taken of that item
# final_str =  re.sub('\u200f', "",(re.sub('\u200e', "", item['Date taken'])))




