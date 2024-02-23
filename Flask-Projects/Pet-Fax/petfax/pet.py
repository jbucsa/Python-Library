from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def get_pet(id):
    pet = next(filter(lambda x: x['pet_id'] == id, pets), None)
    return render_template('pet.html', pet=pet) 

@bp.route('/fact_submit')
def fact_submit():
    return render_template('fact_submit.html')