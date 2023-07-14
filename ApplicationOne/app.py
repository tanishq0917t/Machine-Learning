from flask import *
import sklearn.datasets
import statistics
import numpy
def myFunc(a):
    return a[0]


def knn(dataSet,target):
    limit=int(len(dataSet)*0.8)
    testDataSet=dataSet[0:limit]
    queryDataSet=dataSet[limit:]
    testTarget=target[0:limit]
    queryTarget=target[limit:]
    print("Test DataSet:",testDataSet)
    print("Test Target:",testTarget)
    n=int(len(testDataSet)**0.5)
    if n%2==0: n+=1
    ansList=[]
    for idx in range(len(queryDataSet)):
        queryData=queryDataSet[idx]
        frequencyList=[]
        # print("Querying For:",queryData)
        for indx in range(len(testDataSet)):
            testData=testDataSet[indx]
            tTarget=testTarget[indx]
            frequencyList.append((((testData[0]-queryData[0])**2+(testData[1]-queryData[1])**2)**0.5,tTarget))
        print("Before Sorting")
        print(frequencyList)
        print("After Sorting")
        frequencyList.sort(key=myFunc)
        print(frequencyList)
        print("After slicing by 'n'")
        frequencyList=frequencyList[:n]
        mm=[]
        for i in frequencyList:
            mm.append(i[1])
        ansList.append(statistics.mode(mm))
        print(frequencyList)
        print()
    return ansList


app = Flask(__name__)
@app.route('/')
def serveIndex():
    # set,target=sklearn.datasets.make_blobs(n_samples=100,centers=2,n_features=2)
    # set=set.tolist()
    # target=target.tolist()
    # my_list = [set,target]
    # return render_template('index.html',my_list=my_list)
    return render_template('index.html')

@app.route('/genDataSet',methods=['GET','POST'])
def provideDataSet():
    if request.method=="POST":
        rows=request.form['rows']
        algo=request.form['algo']
        print(rows,algo)
        if algo=="1":
            set,target=sklearn.datasets.make_blobs(n_samples=int(rows),centers=2,n_features=2)
            set=set.tolist()
            target=target.tolist()
            a={'dataSet':set,'target':target}
            return jsonify(a)
@app.route('/processRecords',methods=['GET','POST'])
def process():
    if request.method=="POST":
        # dataSet=request.form['dataSet']
        # target=request.form['target']
        # print(dataSet)
        # print(target)
        a=request.form
        x=0
        for key, value in a.items():
            data=json.loads(key)
        return jsonify(knn(data['dataSet'],data['target']))
if __name__ == '__main__':
    app.run(debug = True)

