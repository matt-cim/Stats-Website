from flask import Blueprint, render_template, request
import statistics

pages = Blueprint(__name__, "pages")

# home page
@pages.route('/')
def home():
    return render_template('skeleton.html')

# page for single data set
@pages.route('/pages/statistics/', methods = ['POST', 'GET'])
def stats():
    if request.method == 'GET':
        # user tried accessing results before inputting data
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
        return render_template("skeleton.html", stdev = f'{round(statistics.stdev(int_list), 2)}', 
                                                variance = f'{round(statistics.variance(int_list), 2)}',
                                                median = f'{round(statistics.median(int_list), 2)}',
                                                mode = f'{statistics.mode(int_list)}')

# page for two data sets
@pages.route('/pages/twosets/', methods = ['POST', 'GET'])
def twoSets():
    if request.method == 'GET':
        return f"please enter data before finding statistics please"
    if request.method == 'POST':
        input1 = request.form.get("input1")
        input2 = request.form.get("input2") 
        # separating the two data sets into variables
        x = list(map(int,input1.split()))
        y = list(map(int,input2.split()))
        return render_template("skeleton.html", covariance = f'{round(statistics.covariance(x, y), 2)}',
                                                correlation = f'{round(statistics.correlation(x, y), 2)}')