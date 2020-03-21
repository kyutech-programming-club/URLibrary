from main.models import db, User, Url, Favo
import random, string

def make_url(n):
    urls = []
    for i in range(n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(20)]
        urls.append(''.join(randlst))
        
    return urls

users = ["A", "B", "C", "D", "E", "F"]
urls = make_url(20)
print(urls)

for user in users:
    db.session.add(User(name=user))
    db.session.commit()

for ur in urls:
    url = Url(maker=users[random.randint(0,5)], url=ur, title=ur+"のリンク")
    db.session.add(url)
    db.session.commit()

for i in range(20):
    favo = Favo(user_id=random.randint(0,5), url_id=i)
    db.session.add(favo)
    db.session.commit()
