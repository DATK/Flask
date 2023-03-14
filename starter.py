from src import site_1 as s
from src import sh
from flask import Flask, request, redirect, render_template, session, url_for
from src import mas_sort as ms

c = s.Reg_or_chek_reg("data.txt")
mas = list()


def passwor_shifr(pas):
    c_sh = sh.cezar(text=pas, key=3)
    sh.cls()
    return c_sh


def chek(pas):
    c_shi = sh.cezar_unsc(text=pas, key=3)
    sh.cls()
    return c_shi


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/main")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return "Вы авторизовались"


@app.route("/reg/", methods=["GET", "POST"])
@app.route("/reg", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        user = request.form['username']
        pas = request.form["password"]

        if c.chek_reg(user) == False:
            c.reg(user, passwor_shifr(pas))
            return redirect("/")
        else:
            return redirect("/reg")
    else:
        return render_template("reg.html")


@app.route('/vhod', methods=["GET", "POST"])
@app.route('/vhod/', methods=["GET", "POST"])
def vhod():
    if request.method == "POST":
        user = request.form["username"]
        pasd = request.form["password"]
        if c.vhode(user, passwor_shifr(pasd)) == True:
            session['username'] = request.form['username']
            return redirect("/profile")
        else:
            return redirect("/vhod")
    else:
        return render_template("vhod.html")


@app.route('/clear/sessions/r328jifs')
def logout():
    session.pop('username', None)
    return redirect(url_for('index.html'))



app.run(debug=True)
