from flask import Flask,render_template
import pandas as pd
import geopandas  as gpd
import contextily
import matplotlib.pyplot as plt
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def hello_world():
    df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name='products')
    
    return render_template('index1.html',df=df.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma