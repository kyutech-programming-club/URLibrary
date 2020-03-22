from main import app
from flask import request, redirect, url_for, render_template, flash, session
from main.models import db, User, Url, Favo

color = [
    "blue","yellow","red","lime",
    "purple","aqua","black","navy","gray",
    "silver", "teal","fuchsia","olive","white"
]

@app.route("/")
def show_entries():
    # loginしていないときの処理（loginしていないときloginフォームへリダイレクト）
    if not session.get("user_id"):
        #print("session is none")
        return redirect(url_for("create_user"))
    users = User.query.all()
    user_names = []

    for user in users:
        user_names.append(user.name)
    
    color_dict = dict(zip(user_names, color))
    urls = Url.query.order_by(Url.id.desc()).all()

    favos = Favo.query.filter_by(user_id=session.get("user_id")).all()
    favo_urls = []
    for favo in favos:
        favo_urls.append(Url.query.filter_by(id=favo.url_id).first())

    return render_template("index.html", urls=urls, favos=favo_urls, color=color_dict)

# /loginにリクエストがあったときのルーティング (GET,POST つかいますよーっって感じ)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': #もしPOSTリクエストがあったとき
        user = User.query.filter_by(name=request.form["username"]).first()
        if user is None:
            print('ユーザ名が異なります')
            return render_template('login.html')
            #GETメソッドの場合は（/loginにアクセスされたとき） render_template('login.html') が実行されてログインページへ
        else:
            session["user_id"] = user.id
            return redirect(url_for('show_entries')) #username,passwordが両方あってるとき、ページ飛んで終わり

    return render_template('login.html')
    #GETメソッドの場合は（/loginにアクセスされたとき） render_template('login.html') が実行されてログインページへ


@app.route("/first_page", methods = ["GET","POST"])
def create_user():
    if request.method == "POST":
        user = User(name = request.form["username"])
        if User.query.filter_by(name=request.form["username"]).first():
            print("同じ名前がすでに存在しています")
            return render_template("first_page.html")
        else:
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            return redirect(url_for("show_entries"))
    else:
        return render_template("first_page.html")

@app.route('/logout')
def logout():
    session.pop("user_id",None) #session情報を削除
    return redirect(url_for("show_entries"))

@app.route("/howto")
def howto():
    return render_template("howto.html")

@app.route('/debug', methods= ['POST', 'GET'])
def print_debug():
    if request.method == 'POST':
        data = dict(request.form)
        user_id = User.query.filter_by(id=data["name"]).first()
        db.session.add(Url(maker=data["name"], url=data["url"], title=data["title"]))
        db.session.commit()

    return 'ディーバっく'

@app.route('/favo')
def favo():
    user_id = int(request.args.get('user_id'))
    url_id = int(request.args.get('url_id'))

    print(user_id, url_id)
    favo = Favo(user_id=user_id, url_id=url_id)
    db.session.add(favo)
    db.session.commit()

    print("save")
    
    users = User.query.all()
    user_names = []

    for user in users:
        user_names.append(user.name)
    
    color_dict = dict(zip(user_names, color))
    urls = Url.query.order_by(Url.id.desc()).all()

    favos = Favo.query.filter_by(user_id=session.get("user_id")).all()
    favo_urls = []
    for favo in favos:
        favo_urls.append(Url.query.filter_by(id=favo.url_id).first())

    return render_template('index.html', urls=urls, favos=favo_urls, color=color_dict)
