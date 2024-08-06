import os
import numpy as np
import pandas as pd
from PIL import Image
from keras.applications.vgg16 import VGG16, preprocess_input
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf
load_img = tf.keras.preprocessing.image.load_img
img_to_array = tf.keras.preprocessing.image.img_to_array
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle


# Datset path
data_dir = "./static"
violent_dir = os.path.join(data_dir, "violence")
non_violent_dir = os.path.join(data_dir, "non-violence")
images_dir = os.path.join(data_dir, "testIMG")

# Charger les images et extraire les caractéristiques avec VGG16
model = VGG16(weights='imagenet', include_top=False)


def getFeatures(image_name):
    # Datset path
    data_dir = "./static/"
    images_dir = os.path.join(data_dir, "images/testData")

    # Charger les images et extraire les caractéristiques avec VGG16
    model = VGG16(weights='imagenet', include_top=False)

    img = Image.open(os.path.join(images_dir, image_name)).resize((224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    print("shape : ",x.shape)
    features = model.predict(x)
    features_vector = features.flatten()
    features_vector = np.append(features_vector, 0)

    return features_vector

def getDisease(vector):
    with open('static/model/svm/svm_RGBmodel.pkl', 'rb') as f:
        clf = pickle.load(f)

    print("=================> the vector : ",vector)
    result = clf.predict([vector])
    return result