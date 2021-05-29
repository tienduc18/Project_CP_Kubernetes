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
        return render_template('index.html')

@app.route('/deploy_redis', methods=['POST','GET'])
def Trang2():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Deploy redis using Helm':
            output = os.system('helm repo add bitnami https://charts.bitnami.com/bitnami')
            output = os.system('helm install redis bitnami/redis')
            list = os.popen('helm ls').readlines()
            matrix = []
            for i in list:
                ls  = i.replace(" ", "").split('\t')
                ls[len(ls)-1] = ls[len(ls)-1][-2]
                matrix.append(ls)
            print(matrix)
            return render_template('Trang2.html', mydata = matrix[1:len(matrix)])
        elif request.form['submit_button'] == 'Delete redis application using Helm':
            output = os.system('helm delete redis')
            return render_template('Trang1.html')
    else:
        return render_template('Trang1.html')

@app.route('/deploy_spark', methods=['POST','GET'])
def Trang3():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Deploy spark using Helm':
            output = os.system('helm repo add bitnami https://charts.bitnami.com/bitnami')
            output = os.system('helm install spark bitnami/spark')
            list = os.popen('helm ls').readlines()
            matrix = []
            for i in list:
                ls  = i.replace(" ", "").split('\t')
                ls[len(ls)-1] = ls[len(ls)-1][-2]
                matrix.append(ls)
            print(matrix)
            return render_template('Trang3.html', mydata = matrix[1:len(matrix)])
        elif request.form['submit_button'] == 'Delete spark application using Helm':
            output = os.system('helm delete spark')
            return render_template('Trang1.html')
    else:
        return

if __name__ == "__main__":
    app.run()