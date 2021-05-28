from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/vmd_timestamp1')
def vmd_timestamp():
    return render_template('Trang1.html')

@app.route('/vmd_timestamp2')
def Trang2():
    contex = {
        "pod1":"NGINX1",
        "Status1":"READY",
        "Age1":"12s",
        "pod2":"NGINX2",
        "Status2":"READY",
        "Age2":"23s",
    }
    return render_template('Trang2.html', mydata = contex)

@app.route('/vmd_timestamp3')
def Trang3():
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

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)