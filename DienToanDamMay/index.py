from flask import Flask, render_template, redirect, url_for, request
import os
import subprocess
import sys

app = Flask(__name__)

def RunCommand(command):
    result = os.popen(command).read();
    return result

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/deploy_apps', methods=['POST','GET'])
def vmd_timestamp():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Start cluster':
            output = os.system('minikube start')
            return render_template('Trang1.html')
        elif request.form['submit_button'] == 'Stop cluster':
            output = os.system('minikube stop')
            return render_template('index.html')
        elif request.form['submit_button'] == 'Delete cluster':
            output = os.system('minikube delete')
            return render_template('index.html')
    else:
        return

@app.route('/deploy_nginx', methods=['POST','GET'])
def Trang2():
    if request.method == 'POST':
        list = os.popen('helm ls').readlines()
        matrix = []
        for i in list:
            ls  = i.replace(" ", "").split('\t')
            ls[len(ls)-1] = ls[len(ls)-1][-2]
            matrix.append(ls)
        print(matrix)
        contex = {
            "pod1":"NGINX1",
            "Status1":"READY",
            "Age1":"12s",
            "pod2":"NGINX2",
            "Status2":"READY",
            "Age2":"23s",
        }
        return render_template('Trang2.html', mydata = contex)
    else:
        return

@app.route('/deploy_spark', methods=['POST','GET'])
def Trang3():
    if request.method == 'POST':
        list = os.popen('helm ls').readlines()
        matrix = []
        for i in list:
            ls  = i.replace(" ", "").split('\t')
            ls[len(ls)-1] = ls[len(ls)-1][-2]
            matrix.append(ls)
        print(matrix)
        contex = {
            "pod1":"spark_master_0",
            "Status1":"READY",
            "Age1":"12s",
            "pod2":"spark_worker_0",
            "Status2":"READY",
            "Age2":"23s",
            "pod3": "spark_worker_1",
            "Status3": "READY",
            "Age3": "45s",
        }
        return render_template('Trang3.html', mydata = contex)
    else:
        return

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)