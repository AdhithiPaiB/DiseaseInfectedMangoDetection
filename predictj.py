# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:06:50 2020

@author: Lenovo
"""

import cv2  # working with, mainly resizing, images
import numpy as np  # dealing with arrays
import os  # dealing with directories

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf
import argparse
#import imutils 
#from keras.models import load_model

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to our input image")
args = vars(ap.parse_args())


def analysis():
    
    img = args["image"]
    IMG_SIZE = 50
    LR = 1e-3 
    MODEL_NAME = 'healthyvsunhealthy-{}-{}.model'.format(LR, '2conv-basic')

    def process_verify_data(img):
        verifying_data = []
        # for img in tqdm(os.listdir(verify_dir)):
        path = img
        img_num = img.split('.')[0] #split
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        verifying_data.append([np.array(img), img_num]) #save image (fullname),without jpg
        np.save('verify_data.npy', verifying_data)
        return verifying_data

    verify_data = process_verify_data(img)
    # verify_data = np.load('verify_data.npy')

    
    tf.reset_default_graph() 

    convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

    convnet = conv_2d(convnet, 32, 3, activation='relu') #cnn layers
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 128, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 32, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 4, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_dir='log')

    if os.path.exists('{}.meta'.format(MODEL_NAME)):
        model.load(MODEL_NAME)
        print('model loaded!')

   
   

    for num, data in enumerate(verify_data):

        img_num = data[1]
        img_data = data[0]

        # y = fig.add_subplot(3, 4, num + 1)
        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)
        # model_out = model.predict([data])[0]
        model_out = model.predict([data])[0]
    
        if np.argmax(model_out) == 0:
            str_label = 'Healthy'
        #elif np.argmax(model_out) == 1 :
            #str_label = 'Unhealthy'
       # elif np.argmax(model_out) == 2:
        #    str_label = 'Unhealthy'
        #elif np.argmax(model_out) == 3:
         #   str_label = 'Unhealthy'

        # if str_label =='Healthy':
        #     status ="HEALTHY"
        else:
              str_label= "Unhealthy"

        print(str_label)

analysis() 