from flask import Blueprint, render_template, request
import statistics

pages = Blueprint(__name__, "pages")

@pages.route('/')
def home():
    return render_template('skeleton.html')
 
@pages.route('/statistics/', methods = ['POST', 'GET'])
def stats():
    if request.method == 'GET':
        return f"please enter data before finding statistics please"
    if request.method == 'POST':
        inputs = request.form.get("input") 
        # put a ',' inside split if want to seperate by commas
        int_list = list(map(int,inputs.split()))
        list_len = len(int_list)
        sum = 0
        # computing sum
        for numbers in int_list:
            sum += numbers
        return render_template("skeleton.html", mean = f'{sum/list_len}', 
                                                median = f'{statistics.median(int_list)}',
                                                sum = f'{sum}',
                                                mode = f'{statistics.mode(int_list)}')

@pages.route('/twosets/', methods = ['POST', 'GET'])
def twoSets():
    if request.method == 'GET':
        return f"please enter data before finding statistics please"
    if request.method == 'POST':
        input1 = request.form.get("input1")
        input2 = request.form.get("input2") 
        x = list(map(int,input1.split()))
        y = list(map(int,input2.split()))
        return render_template("skeleton.html", covariance = f'{statistics.covariance(x, y)}')

@pages.route('/child/')
def child():
    return render_template('child.html')