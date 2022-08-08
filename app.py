from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase(
  'dark-souls-bosses',
  user='mraznick',
  password='',
  host='localhost',
  port=5432
)

class BaseModel(Model):
  class Meta:
    database = db