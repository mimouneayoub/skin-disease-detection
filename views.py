from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from cnn import getDisease, getFeatures
import numpy as np

views = Blueprint(__name__,"views")

@views.route("/home")
def home():
    mynotification=session.get('notification')
    result=session.get('result')
    mysourceImg=session.get('sourceImg')
    disease = session.get('disease')
    return render_template("index.html",result=result,notification=mynotification,sourceImg=mysourceImg,disease=disease)  


@views.route("/predictor",methods=['POST','GET'])
def predict():  
    args = request.form
    print("======> the args : ",args)
    img=request.files['image']

    #///////////////// Prediction /////////////////#
    # mask = predictMask(img.filename)
    features_vector = getFeatures(img.filename) 
    diseaseNumber = getDisease(features_vector)
    print("diease number ========================== : ",diseaseNumber)
    disease = getDiseaseFromNumber(diseaseNumber)
    #///////////////// Prediction /////////////////#

    session['disease']=disease
    session['sourceImg']=img.filename
    img.save('static/uploads/' + img.filename)
    session['result']='Based on the analysis of the provided image, it appears that you may have '
    return redirect(url_for('views.home')) 

def getDiseaseFromNumber(number):
    print('===================================> the number : ',number)
    number = number[0]
    print(number)
    if number==0: return "Actinic keratoses (akiec)"
    elif number==1: return "Basal cell carcinoma (bcc)"
    elif number==2: return "Benign keratosis-like lesions (bkl)"
    elif number==3: return "Dermatofibroma (df)"
    elif number==4: return "Melanoma (mel)"
    elif number==5: return "Melanocytic nevi (nv)"
    elif number==6: return "Vascular lesions (vas)"
    else: return "Error !"