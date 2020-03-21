from main import app
from flask import request, redirect, url_for, render_template, flash, session
from main.models import db, User

@app.route("/")
def show_entries():
    # loginしていないときの処理（loginしていないときloginフォームへリダイレクト）
    if not session.get("user_id"):
        #print("session is none")
        return redirect(url_for("login"))
    return render_template("index.html")

# /loginにリクエストがあったときのルーティング (GET,POST つかいますよーっって感じ)
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST': #もしPOSTリクエストがあったとき
        user  = User.query.filter_by(name=request.form["username"]).first()
        if user is None:
            print('ユーザ名が異なります')
            return render_template('login.html')
            #GETメソッドの場合は（/loginにアクセスされたとき） render_template('login.html') が実行されてログインページへ
        else:
            session["user_id"] = user.id
            return redirect(url_for('show_entries')) #username,passwordが両方あってるとき、ページ飛んで終わり

    return render_template('login.html')
    #GETメソッドの場合は（/loginにアクセスされたとき） render_template('login.html') が実行されてログインページへ

@app.route('/logout')
def logout():
    session.pop("user_id",None) #session情報を削除
    return redirect(url_for("show_entries"))
