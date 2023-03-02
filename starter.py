from src import site_1 as s
from src import sh
from flask import Flask, request, redirect, render_template

c = s.Reg_or_chek_reg("data.txt")
voshel=False

def passwor_shifr(pas):
    c_sh = sh.cezar(text=pas, key=3)
    sh.cls()
    return c_sh
#это функции ширфрования и дешифрования пароля которые основываются на моих методах шифрования


def chek(pas):
    c_shi = sh.cezar_unsc(text=pas, key=3)
    sh.cls()
    return c_shi

reght=s.read_html("reg.html")
vhodht=s.read_html("vhod.html")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/reg', methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        c.reg(username,passwor_shifr(password))
        return redirect("/")
    else:
        return reght

@app.route('/vhod', methods=["GET", "POST"])
def signup():
    global voshel
    if request.method == "POST":
        user = request.form["username"]
        pas = request.form["password"]
        if c.vhode(user,passwor_shifr(pas))==True:
            voshel=True
            return redirect("/reg")
        else:
            return redirect("/")
    else:
        return vhodht
    
app.run(debug=True)

