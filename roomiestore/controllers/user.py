# for typing purposes
from ..db import DB
import datetime

class UserController:
    def __init__(self, logger, db, user_model):
        self._logger = logger
        self._db: DB = db
        self._Model = user_model

    def get_user_by_id(self, user_id):
        return self._db.query(self._Model).filter_by(user_id=user_id).all()

    def add(self, fname, lname, dob, email, phone, username, passwd, role_id):
        now = datetime.datetime.now()
        user = self._Model(
            fname=fname,
            lname=lname,
            dob=dob,
            email=email,
            phone=phone,
            username=username,
            password=passwd,
            date_created=now,
            last_updated=now,
            role_id=role_id)
        self._db.add(user)