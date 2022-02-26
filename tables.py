from sqlalchemy import MetaData, Table, String, Integer, Column, DateTime, Boolean, ForeignKey
from datetime import datetime

metadata = MetaData()

users = Table('users', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('login', String(256), nullable=False),
    Column('password', String(256),  nullable=False),
    Column('name', String(256), nullable=False),
    Column('last_visit', DateTime(), default=datetime.now, onupdate=datetime.now)
)

message_groups = Table('message_groups', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('name', String(256), nullable=False),
    Column('create', DateTime(), default=datetime.now)
)

message_group_users = Table('message_group_users', metadata, 
    Column('id_user', ForeignKey('users.id')),
    Column('id_group', ForeignKey('message_groups.id'))
)

messages = Table('messages', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('id_group', ForeignKey('message_groups.id')),
    Column('m_data', String(1024), nullable=False),
    Column('m_time', DateTime(), nullable=False, default=datetime.now)
)