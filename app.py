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


class Boss(BaseModel):
    name = CharField()
    ngHealth = CharField()
    drops = CharField()


Boss(name='Asylum Demon', ngHealth=825,
     drops='2000 souls, 1 Humanity, Big Pilgrim\'s Key, chance to drop Demon\'s Great Hammer').save()
Boss(name='Bell Gargoyles', ngHealth=3700,
     drops='10,000 souls, 1 Twin Humanities; Chance to drop Gargoyle Halberd/Shield/Help/Tail Axe').save()
Boss(name='Capra Demon', ngHealth=1176,
     drops='6,000 souls, Key to Depths, 1 Humanity, 1 Homeward Bone, chance to drop Demon Great Machete').save()
Boss(name='Centipede Demon', ngHealth=3432,
     drops='40,000 souls, Orange Charred Ring, 1 Humanity, 1 Homeward Bone').save()
Boss(name='Chaos Witch Quelaag', ngHealth=3139,
     drops='Soul of Quelaag, 20,000 souls, 1 Twin Humanities').save()
Boss(name='Dark Sun Gwyndolin', ngHealth=2000,
     drops='Soul of Gwyndolin, 40,000 souls')

app = Flask(__name__)


@app.route('/bosses/', methods=['GET', 'POST'])
@app.route('/bosses/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Boss.get(Boss.id == id)))
        else:
            boss_list = []
            for boss in Boss.select():
                boss_list.append(model_to_dict(boss))
            return jsonify(boss_list)

    if request.method == 'PUT':
        return 'PUT request'
