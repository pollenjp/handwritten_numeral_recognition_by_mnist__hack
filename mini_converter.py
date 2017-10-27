# encoding: utf-8


import os
import uuid
from PIL import Image
from array import *



def convert(one_file_name, output_filename):
    '''
    file_name = 'hoge/hoge.png'
    '''

    data_image = array('B')
    data_label = array('B')
    FileList = []
    FileList.append(one_file_name)
    for file_name in FileList:
        #label = int(file_name.split("/")[1])
        Im = Image.open(file_name)
        pixel = Im.load()
        width, height = Im.size
        for x in range(0,width):
            for y in range(0,height):
                data_image.append(pixel[y,x])
        #data_label.append(label) # labels start (one unsigned byte each)
    hexval = "{0:#0{1}x}".format(len(FileList),6) # number of files in HEX

    # header for label array
    header = array('B')
    header.extend([0,0,8,1,0,0])
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[2:][2:],16))

    #data_label = header + data_label

    # additional header for images array
    if max([width,height]) <= 256:
        header.extend([0,0,0,width,0,0,0,height])
    else:
        raise ValueError('Image exceeds maximum size: 256x256 pixels');
    header[3] = 3 # Changing MSB for image data (0x00000803)

    data_image = header + data_image

    output_file = open( output_filename, 'wb')
    data_image.tofile(output_file)
    output_file.close()

    #output_file = open( 'www_save/test-labels-idx1-ubyte', 'wb')
    #data_label.tofile(output_file)
    #output_file.close()

    #os.system('gzip -f www_save/test-images-idx3-ubyte')



