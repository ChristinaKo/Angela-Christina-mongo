from flask import Flask, render_template, request,redirect, session, url_for
import MongoWork
app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
    try:
        reged = registered
    except NameError:
        reged=False
    return render_template("index.html",reged=reged)

@app.route("/about", methods=["POST","GET"])
def about():
    return render_template("about.html")

@app.route("/loggedin/<username>")
def logged_in(username):
    return render_template("loggedin.html")
    
@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        usr = request.form['username']
        passw = request.form['passwd']
        repassw = request.form['repasswd']
        firstname = request.form['fname']
        lastname = request.form['lname']
        if passw == repassw and usr!='' and passw!='' and firstname!='' and lastname!='':#checks if everything is filled out
            registered=True
            #retVals = ' %s , %s, %s, %s , %s ' % (usr, passw, repassw, firstname, lastname)
            mongo_input = { 'uname':usr,
                            'password':passw, 
                            'firstname':firstname,
                            'lastname':lastname } 
            #print mongo_input
            print MongoWork.check_user_in_db(usr)
            if MongoWork.check_user_in_db(usr):#may change to flash
                user_taken=True
                return render_template("register.html",user_taken=user_taken, usr=usr)
            else:
                MongoWork.new_user(mongo_input) #put user into our mongodb
                return redirect("/") 
        else: #aka passwd !=repassw
            reg_error = True
            #set boolean to true --> will trigger error banner which we will pass through render_template
            return render_template("register.html", reg_error= reg_error)
    return render_template("register.html")#redirect to login, with banner that says "THANK YOU FOR REGISTERING!"

if __name__ == '__main__':
    app.debug = True
    app.run()
