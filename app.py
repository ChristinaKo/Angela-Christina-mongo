from flask import Flask, render_template, request,redirect, session, url_for,session,escape,request
import MongoWork
app = Flask(__name__)
app.secret_key = 'Really secret but not really' #just for session usage


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == 'POST':
        userinput = request.form['user']
        pwdinput = request.form['passwd']
        #print MongoWork.check_user_in_db(userinput)
        if MongoWork.check_user_in_db(userinput) != None:
            if MongoWork.find_pword(userinput) == pwdinput:
                 #session['username'] = request.form['user']
                 return redirect(url_for('about'))
            else:
                error = True
                return render_template("index.html" ,error=error)
        else:
            #print "not in users"
            notreg = True
            return render_template("index.html", notreg = notreg)
    else:#request.method == "GET"
        error = False
        return render_template("index.html")

#can be viewed without logging in
@app.route("/about", methods=["POST","GET"])
def about():
    return render_template("about.html")

@app.route("/loggedin/<username>")
def logged_in(username):
    return render_template("loggedin.html",username=username)

#must pop off session
@app.route("/logout")
def logout():
    return redirect(url_for('index'))
        
@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        usr = request.form['username']
        passw = request.form['passwd']
        repassw = request.form['repasswd']
        firstname = request.form['fname']
        lastname = request.form['lname']
        if passw == repassw and usr!='' and passw!='' and firstname!='' and lastname!='':#checks if everything is filled out
            #retVals = ' %s , %s, %s, %s , %s ' % (usr, passw, repassw, firstname, lastname)
            mongo_input = { 'uname':usr,
                            'password':passw, 
                            'firstname':firstname,
                            'lastname':lastname } 
            #print mongo_input
            #print MongoWork.check_user_in_db(usr)
            if MongoWork.check_user_in_db(usr):
                user_taken=True
                return render_template("register.html",user_taken=user_taken, usr=usr)
            else:####SUCCESS!
                MongoWork.new_user(mongo_input) #put user into our mongodb
                registered = True
                return redirect(url_for("index",registered=registered)) 
        else: #aka passwd !=repassw OR not all filled out
            if passw != repassw:#pwd and re-type pwd fields do not match
                reg_error = True
                return render_template("register.html", reg_error=reg_error)
            else:#missing field error
                empty=True
                return render_template("register.html", empty=empty)
    else:#GET method
        return render_template("register.html")





if __name__ == '__main__':
    app.debug = True
    app.run()
