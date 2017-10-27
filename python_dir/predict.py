# coding: utf-8
import numpy as np
from python_dir.layers import *
from python_dir.gradient import numerical_gradient
from collections import OrderedDict

paramW1 = np.loadtxt("python_dir/paramW1.py", delimiter=",")
paramb1 = np.loadtxt("python_dir/paramb1.py", delimiter=",")
paramW2 = np.loadtxt("python_dir/paramW2.py", delimiter=",")
paramb2 = np.loadtxt("python_dir/paramb2.py", delimiter=",")


layers = OrderedDict()
layers['Affine1'] = Affine(paramW1, paramb1)
layers['Relu1'] = Relu()
layers['Affine2'] = Affine(paramW2, paramb2)
        
def predict(x):
    for layer in layers.values():
        x = layer.forward(x)
    return np.argmax(x)
