from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3 as sql
app = Flask(__name__)
app.secret_key='Bobby@0559'

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/tasks')
def tasks():
    con=sql.connect("data.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM Tasks")
    data=cur.fetchall()
    con.close()
    return render_template("tasks.html", datas = data)

@app.route('/addtask', methods=['POST','GET'])
def addtask():
    if request.method=='POST':
        description=request.form['description']
        con=sql.connect("data.db")
        cur=con.cursor()
        cur.execute("INSERT INTO Tasks (DESCRIPTION) values (?)", (description,))
        con.commit()
        con.close()
        flash('Task Added','success')
        return redirect(url_for('tasks'))
    return render_template("addtask.html")

@app.route("/edittask/<string:tid>",methods=['POST','GET'])
def edittask(tid):
    if request.method=='POST':
        description=request.form['description']
        con=sql.connect("data.db")
        cur=con.cursor()
        cur.execute("UPDATE Tasks SET DESCRIPTION=? where TID=?", (description, tid))
        con.commit()
        con.close()
        flash('Task Updated','success')
        return redirect(url_for("tasks"))
    con=sql.connect("data.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM Tasks WHERE TID=?", (tid,))
    data=cur.fetchone()
    con.close()
    return render_template("edittask.html",datas = data)

@app.route("/deletetask/<string:tid>",methods=['GET'])
def deletetask(tid):
    con=sql.connect("data.db")
    cur=con.cursor()
    cur.execute("DELETE FROM TASKS WHERE TID=?",(tid,))
    con.commit()
    con.close()
    flash('Task Deleted','warning')
    return redirect(url_for("tasks"))

if __name__ == "__main__":
    app.run(debug=True)
    