from flask import Flask, render_template, request,redirect, session

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")


@app.route("/about", methods=["POST","GET"])
def about():
    return render_template("about.html")

#same as index page
@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("index.html")

@app.route("/loggedin/<username>")
def logged_in(username):
    return render_template("loggedin.html")
    
@app.route("/register", methods=["POST","GET"])
def register():
    #use a boolean later/redirect to home page?
    if request.method == "POST":
        usr = request.form['username']
        passw = request.form['passwd']
        repassw = request.form['repasswd']
        firstname = request.form['fname']
        lastname = request.form['lname']
        if passw == repassw and usr!='' and passw!='' and firstname!='' and lastname!='':
            retVals = ' %s , %s, %s, %s , %s ' % (usr, passw, repassw, firstname, lastname)
            MONGO = "{ 'uname':%s } " % (usr)
            return redirect("/") 
        #print retVals
        else: #aka passwd !=repassw
            reg_error = True
            #set boolean to true --> will trigger error banner which we will pass through render_template
            return render_template("register.html")
    return render_template("register.html")#redirect to login, with banner that says "THANK YOU FOR REGISTERING!"

if __name__ == '__main__':
    app.debug = True
    app.run()
