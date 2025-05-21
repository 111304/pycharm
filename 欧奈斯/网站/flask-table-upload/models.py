# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UploadedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column1 = db.Column(db.String(255))
    column2 = db.Column(db.String(255))
    column3 = db.Column(db.String(255))
    # 根据你的表格列添加更多字段