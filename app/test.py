from app import create_app, db
from app.models import Bla

app = create_app()


# def test_create():
#     app.app_context().push()
#     name = ['李靖', '李俊剑', '孙广全']
#     address = ["上海", "上海周边", "其它"]
#     conn = db.session()
#     for n, a in zip(name, address):
#         bla = Bla(name=n, address=a)
#         conn.add(bla)
#         bla.address = a
#         conn.commit()
#         assert bla.name == n


def test_query():
    app.app_context().push()
    bla = Bla.query.filter_by(name="李靖").first()
    assert bla.name == "李靖"
    assert bla.address == "上海"


def test_error():
    app.app_context().push()
    bla = Bla(name="戚红", address="南京")
    conn = db.session()
    conn.add(bla)
    conn.commit()


def test_route():
    pass