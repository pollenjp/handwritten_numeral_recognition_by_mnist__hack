#!/usr/bin/python3
# coding: utf-8

#import cgitb
#cgitb.enable()

import cgi
import base64
from PIL import Image
from PIL import ImageOps
import mini_converter
import mnist
from python_dir.predict import predict
import uuid
import os

###################################
########### html
########################
html_file = open('html_file.html', 'rt')
html_body = ""
for line in html_file:
    html_body += line

#################################
# Python 
#################################
# get png file
form = cgi.FieldStorage()
form_keys = form.keys()
form_value = ""
if "picdata" in form:
    form_value = form["picdata"].value
form_value2 = ""
if "picdata2" in form:
    form_value2 = form["picdata2"].value
form_value3 = ""
input_data_str = ""
result = ""
head = ""
tail = ""
if "picdata3" in form:
    form_value3 = form["picdata3"].value

    arr = form_value3
    arr = arr.split(",")
    if len(arr) >= 2:
        arr = arr[1]
        #img_org_name
        img_org_name = "./www_save/imageToSave" + str(uuid.uuid4()) + ".png"
        fh = open(img_org_name, 'wb')
        fh.write( base64.b64decode(arr) )
        fh.close()

        imgf = img_org_name
        img = Image.open(imgf, 'r')
        resize_img = img.resize( (28, 28) )
        #img_resize_name
        img_resize_name = "./www_save/imageToSave_resize" + str(uuid.uuid4())+ ".png"
        resize_img.save( img_resize_name, "png")
        '''
        grayscale
        '''
        img_gray = img.convert('L' )
        #img_gray_name
        img_gray_name = "./www_save/imageToSave_gray" + str(uuid.uuid4())+ ".png"
        img_gray.save( img_gray_name, "png")

        resize_img_gray = ImageOps.grayscale( resize_img )
        #img_resize_gray_name
        img_resize_gray_name = "./www_save/imageToSave_resize_gray" + str(uuid.uuid4())+ ".png"
        resize_img_gray.save( img_resize_gray_name, "png")

        #img_resize_gray_byte_name
        img_resize_gray_byte_name = "./www_save/test_images-idx3-ubyte" + str(uuid.uuid4())
        mini_converter.convert(img_resize_gray_name, img_resize_gray_byte_name)

        '''
        mnist
        '''
        load_filename = img_resize_gray_byte_name
        #save_filename
        save_filename = "./www_save/mnist" + str(uuid.uuid4()) + "pkl"
        input_data =  mnist.load_mnist(load_filename, save_filename)
        input_data_str = str( input_data )
        result = str( predict(input_data) )
        head = "<h1>You draw number: "
        tail = "</h1>"

        ######################################
        ########    remove file     ########
        ######################################
        os.remove( img_org_name )
        os.remove( img_resize_name )
        os.remove( img_gray_name )
        os.remove( img_resize_gray_name )
        os.remove( img_resize_gray_byte_name )
        os.remove( save_filename )


print("Content-type: text/html\n")
print(html_body % { 'head':head, 'result':result, 'tail':tail } )



