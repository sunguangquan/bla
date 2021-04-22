from app import db
from sqlalchemy import Column, String, Integer, Enum
from app import admin
from flask_admin.contrib.sqla import ModelView


class Bla(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    open_id = Column(String(50), unique=True)
    address = Column(Enum('上海', '上海周边', '其它'))
    other = Column(String(255))

    def __repr__(self):
        return "姓名: {} 地址: {}  建议:{}".format(self.name, self.address, self.other)

    def get_add(self):
        return self.address


admin.add_view(ModelView(Bla, db.session))
