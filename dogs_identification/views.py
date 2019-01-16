from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

from context import learning_models_path, datasources_application
from functions_tailored import predict_dog_race, preprocess_for_vgg16

dogs_data_path = datasources_application

@app.route('/', methods =['GET','POST'])
@app.route('/?', methods =['GET','POST'])
@app.route('/index/', methods =['GET','POST'])
def index(dog=None,results=None):
    if request.method == 'POST':
        dog = request.form['dog']
        print("dog is %s"%dog)

        if len(dog)>0:
            print()
            picture_path = dogs_data_path+dog
            print(picture_path)
            img_for_vgg16 = preprocess_for_vgg16(picture_path)
            results = predict_dog_race(img_for_vgg16)

    return render_template('index.html',dog=dog,results=results)

@app.route('/dogs_list/')
def dogs_list():
    return render_template('dogs_list.html')
