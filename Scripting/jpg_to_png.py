#importing modules

import sys
import os
from PIL import Image

#Get the first and second argument of the exe command.

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in os.listdir(source_folder):
    image = Image.open(f'{source_folder}{file}')
    name_string = os.path.splitext(file)[0]
    image.save(f'{destination_folder}{name_string}.png', 'png')