from ..db import Base
from sqlalchemy import Column, Text, DateTime, BigInteger, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    user_id = Column(BigInteger, primary_key=True)
    fname = Column(Text(length=50), nullable=False)
    lname = Column(Text(length=50), nullable=False)
    dob = Column(DateTime, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text(length=15), nullable=True)
    username = Column(Text(50), nullable=False)
    password = Column(Text(128), nullable=False)
    date_created = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)
    role_id = Column(SmallInteger, ForeignKey('role.role_id'))
    role = relationship('Role', foreign_keys=[role_id])

    def __repr__(self):
        return f'User({self.username},{self.user_id}, {self.role})'


'''
CREATE TABLE "user"
(
 "user_id"      bigserial NOT NULL,
 "fname"        varchar(50) NOT NULL,
 "lname"        varchar(50) NOT NULL,
 "dob"          date NOT NULL,
 "email"        text NOT NULL UNIQUE,
 "phone"        varchar(15) NULL,
 "username"     varchar(50) NOT NULL UNIQUE,
 "password"     varchar(128) NOT NULL,
 "date_created" date NOT NULL,
 "last_updated" date NOT NULL,
 "role_id"      smallint NOT NULL,
 CONSTRAINT "PK_user" PRIMARY KEY ( "user_id" ),
 CONSTRAINT "FK_262" FOREIGN KEY ( "role_id" ) REFERENCES "role" ( "role_id" )
);

CREATE INDEX "fkIdx_262" ON "user"
(
 "role_id"
);

CREATE INDEX "user_email_idx" ON "user"
(
 "email"
);

CREATE INDEX "user_username_idx" ON "user"
(
 "username"
);
'''