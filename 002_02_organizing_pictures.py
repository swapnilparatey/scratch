# Goal is to organize all the pictures that you have
# Read through the meta-data - put it up in sequential folders - depending upon time
# If pictures are from an iPhone or Nexus or GoPro - put them in different folders
# If pictures are memes, snapshots etc. - put them in different folders
# Figure out how to read metadata of different file formats - Image and VIDEO

from exif import Image
import glob
import re
from os import listdir
from os.path import isfile, join
from datetime import datetime
import shutil

directory = "C:\\Users\\linpa\\Desktop\\Crap\\iPhone2020\\DCIM\\100APPLE\\"
destination = "C:\\Users\\linpa\\Desktop\\Sorted_Pics\\"
count = 0

# Figure out how to clean up this function - and write it better later!
def is_iphone_camera_image(exif_image_file):
    try:
        value = False
        if not exif_image_file.has_exif:
            return value
        if (exif_image_file.model == 'iPhone XS') | (exif_image_file.model == 'iPhone 7'):
            if (exif_image_file.pixel_x_dimension == 4032) | (exif_image_file.pixel_x_dimension == 3024):
                if (exif_image_file.pixel_y_dimension == 4032) | (exif_image_file.pixel_y_dimension == 3024):
                    value = True
        return value
    except Exception as e:
        print(e.args)
        return False


# list_of_files = glob.glob(directory)
# print("Total files in this directory = " + str(len(list_of_files)))

# for file_name in list_of_files:
#     print(re.findall(re.escape("*JPG"), file_name))

all_files = [f for f in listdir(directory) if isfile(join(directory, f))]
jpg_files = [file for file in all_files if file.endswith(".JPG")]
mov_files = [file for file in all_files if file.endswith(".MOV")]
mp4_files = [file for file in all_files if file.endswith(".MP4")]
png_files = [file for file in all_files if file.endswith(".PNG")]

for file in jpg_files:
    jpg_file = open(directory + file, 'rb')
    exif_data = Image(jpg_file)
    if is_iphone_camera_image(exif_data):
        # instead of using datetime, why don't we just replace semi-colon and space with _ in the exif string
        # we'll figure that one out later - at the moment - we're happy we used the datetime lib haha
        date_time_data = datetime.strptime(exif_data.datetime_original, "%Y:%m:%d %H:%M:%S")
        output_file_name = datetime.strftime(date_time_data, "%Y_%m_%d_%H_%M_%S")

        # To copy paste files - we have a bunch of options - easiest one is copy2 from shutil
        # http://timgolden.me.uk/python/win32_how_do_i/copy-a-file.html
        shutil.copy2(directory + file, destination + output_file_name[0:4]  + "\\" + output_file_name + ".JPG")
        # shutil.move(directory + file, destination + output_file_name[0:4] + "\\" + output_file_name + ".JPG")
    else:
        print(directory + file + " not processed")
        # Below line needs to be checked - write it differently please!!!
        shutil.copy2(directory + file, destination + "WhatsApp" + "\\" + output_file_name + ".JPG")
    jpg_file.close()
    count += 1

print("Total files processed = ", count)






