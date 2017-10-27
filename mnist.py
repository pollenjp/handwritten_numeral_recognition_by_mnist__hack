# coding: utf-8

import os.path
import gzip
import pickle
import os
import numpy as np


#dataset_dir = 'www_save'
#save_file = dataset_dir + "/mnist.pkl"
img_dim = (1, 28, 28)
img_size = 784
def _load_img(file_name):
    file_path = file_name
    #print("Converting " + file_name + " to NumPy Array ...")    
    with open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, img_size)
    #print("Done")
    return data
def _convert_numpy(load_filename):
    dataset = {}
    dataset['input_img'] =  _load_img(load_filename)
    return dataset

def init_mnist(load_filename, save_file):
    dataset = _convert_numpy(load_filename)
    #print("Creating pickle file ...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)
    #print("Done!")
def load_mnist(load_filename, save_filename, normalize=True, flatten=True):
    """MNISTデータセットの読み込み
    Parameters
    ----------
    normalize : 画像のピクセル値を0.0~1.0に正規化する
    one_hot_label : 
        one_hot_labelがTrueの場合、ラベルはone-hot配列として返す
        one-hot配列とは、たとえば[0,0,1,0,0,0,0,0,0,0]のような配列
    flatten : 画像を一次元配列に平にするかどうか 
    Returns
    -------
    (訓練画像, 訓練ラベル), (テスト画像, テストラベル)
    """
    #if not os.path.exists(save_file):
    init_mnist(load_filename, save_filename)
        
    with open(save_filename, 'rb') as f:
        dataset = pickle.load(f)
    
    if normalize:
        for key in ['input_img']:
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0
    if not flatten:
        for key in ('train_img', 'test_img'):
             dataset[key] = dataset[key].reshape(-1, 1, 28, 28)
    return dataset['input_img']


