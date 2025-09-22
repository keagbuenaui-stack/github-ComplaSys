from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Kenbuena@765",
    database="barangay_system"
)

cursor = connection.cursor()

@app.route("/")
def home_page():
    return render_template("homepage.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/login_process", methods=['POST'])
def login_process():
    user = request.form.get("user_inp")
    password = request.form.get("pass_inp")
    
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (user, password))
    account = cursor.fetchone()

    if account:
        return redirect(url_for("dashboard_page"))
    else:
        return redirect(url_for("login_page"))

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/user_enrolled", methods=['POST'])
def user_enrolled():
    name = request.form.get("name_inp")
    email = request.form.get("email_inp")
    username = request.form.get("user_inp")
    password = request.form.get("pass_inp")

    sql = "INSERT INTO users (full_name, email, username, password) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, username, password))
    connection.commit()

    return redirect(url_for('login_page'))

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/form", methods=["GET", "POST"])
def form_page():
    students = (
        ("Minor", "Male"),
        ("Buena", "Male"),
        ("Richie", "Male")
    )
    return render_template("form.html", info=students)

if __name__ == "__main__":
    app.run(debug=True)
