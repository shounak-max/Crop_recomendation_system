from Flask import Flask, request,render_template
import numpy
import pandas
import sklearn
import pickle
#importing the models

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')




#python main 

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict',methods=['POST'])

def