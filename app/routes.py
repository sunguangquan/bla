from flask import Blueprint, request, jsonify
from app.models import Bla
import requests
from app import db

api = Blueprint('api', __name__)

address = {
    "1": "上海",
    "2": "上海周边",
    "3": "其它"
}


def get_openid(code):
    appid = 'wxcd63e1a3adf67847'
    secret = '4701f27f43992585fd325bbb96c04d2b'
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
        appid, secret, code)
    r = requests.get(url).json()
    openid = r.get("openid")
    return openid


@api.route('/create/row')
def create_row():
    if request.args.get("code"):
        code = request.args.get("code")
        openid = get_openid(code)
        name = request.args.get("name")
        select = request.args.get("select")
        area = request.args.get("area")
        user = Bla.query.filter_by(name=name).first()
        if not user:
            return "error", 700
        if Bla.query.filter_by(open_id=openid).first():
            return "error", 600
        if user.name and not user.open_id:
            user.open_id = openid
            user.address = address.get(select)
            if area:
                user.other = area
            conn = db.session()
            conn.add(user)
            conn.commit()
            return str(user.id), 200
        else:
            return "error", 600


@api.route('/get/all')
def get_all():
    add_list = []
    bla = Bla.query.all()
    for b in bla:
        add_list.append(b.get_add())
    total = len(add_list)
    sh = add_list.count("上海")
    zb = add_list.count("上海周边")
    ot = add_list.count("其它")
    return jsonify({"total": total, "sh": sh, "zb": zb, "ot": ot})
