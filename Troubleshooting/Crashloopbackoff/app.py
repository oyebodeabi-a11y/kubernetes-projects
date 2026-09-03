#from flask import Flask
app = Flask (__name__)


@ app.route("/")
def home():
    return "<h2>Welcome to Kubernetes Ecosystem</h2>"


@ app.route("/hr")
def hr():
    return "<h2>Welcome to Human Resource</h2>"


@ app.route("/reg")
def reg():
    return "<h2>Welcome to Registration</h2>"



@ app.route("/dir")
def dir():
    name = "Abi Oyebode"
    Tel = "07877204616"
    address = "london"
    collect = "The director's details are: " + str(name) + " ," + str(Tel) +  " ," + str(address)
    return collect 


@ app.route("/openings")
def openings():
    first = "Technician"
    second = "Architect"
    third = "DevOps"
    fourth = "Manager"
    collect = "These are the available openings: " + str(first) + ",  " + str(second) + ", " + str(third) + " , " + str(fourth)
    return collect


@ app.route("/add")
def add():
    firstnumber = 89
    secondnumber = 69
    answer = (firstnumber) + (secondnumber)
    return "This is the result of  the addition" + str(answer)


@ app.route("/division")
def divsion():
    firstnumber = 89
    secondnumber = 69
    result = (firstnumber) / (secondnumber)
    return "This is the result of  the divison" + str(result)




#if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
