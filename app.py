from flask import *
app = Flask(__name__) #creating the Flask class object 

import pickle
with open('model_pkl' , 'rb') as f:
    lr = pickle.load(f)
@app.route('/') #decorator defines the 
def home():
    return render_template("predpage.html",pred=0) 

@app.route('/prd',methods=['GET','POST'])
def prd():
    pid=int(request.form['PID'])
    pc=int(request.form['PC'])
    sex=request.form['sex']
    age=float(request.form['age'])
    fare=float(request.form['fare'])
    SbSp=int(request.form['SbSp'])
    parch=int(request.form['parch'])
    emb=request.form['emb']
    l=[pid,pc,age,SbSp,parch,fare]
    if(sex=='male'):
        l.append(1)
    else:
        l.append(0)
    if(emb=='Q'):
        l.append(1)
        l.append(0)
    elif(emb=='S'):
        l.append(0)
        l.append(1)
    else:
        l.append(0)
        l.append(0)
    lr[0].predict([l])[0]
    if(lr==1):
        pr=' SURVIVED'
    else:
        pr='Did not survive!!!!'
    return render_template("predpage.html",pred=pr)

if __name__ =='__main__':  
    app.run(debug = True)