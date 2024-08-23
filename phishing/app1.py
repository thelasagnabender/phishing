from flask import Flask,request
app = Flask(__name__)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred

def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
@app.route('/', methods=['GET', 'POST'])
def index():
    DomainIP = int(request.form.get('Domain_Ip_address'))
    LongUrl = int(request.form.get('Long_URL'))
    Presence1 = int(request.form.get('_@_presence'))
    Presence2 = int(request.form.get('_//_presence'))
    AgeofDomain = int(request.form.get('Age_of_domain'))
    RequestUrl = int(request.form.get('_%_Request_URL'))
    Usingpopup = int(request.form.get('Using_pop_up_or_IFrame'))
    Domainincludes = int(request.form.get('Domain_name_includes'))
    Websitetraffic = float(request.form.get('Website_traffic'))
    p = reg('expense.csv',["Domain_Ip_address","Long_URL,_@_presence","_//_presence,Age_of_domain","_%_Request_URL","Using_pop_up_or_IFrame","Domain_name_includes","Website_traffic"],"outcome",[DomainIP ,LongUrl, Presence1 ,Presence2 ,AgeofDomain ,RequestUrl, Usingpopup, Domainincludes ,Websitetraffic ,AcademicPerformance])
    print("Bot : The Income is: ",float(p[0]))
    p = classify('expense.csv',["Domain_Ip_address","Long_URL,_@_presence","_//_presence,Age_of_domain","_%_Request_URL","Using_pop_up_or_IFrame","Domain_name_includes","Website_traffic"],"outcome",[DomainIP ,LongUrl, Presence1 ,Presence2 ,AgeofDomain ,RequestUrl, Usingpopup, Domainincludes ,Websitetraffic ,AcademicPerformance])
    if int(p[0]) == 0:
        print("Student does not have enough savings")
        pr = "Student does not have enough savings"
    elif int(p[0]) == 1:
        print("Student has enough savings")
        pr = "Student has enough savings"
    return pr

if __name__ == '__main__':
    app.run(debug=True)


