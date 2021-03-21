# web/app.py

import json, os
from flask import request
from . import create_app, database
from .models import Cats

app = create_app()

@app.route('/', methods=['GET'])
def fetch():
    envs = db.get_all(Environments)
    all_envs = []
    for env in envs:
        new_env = {
            "id": env.id,
            "prefix": env.prefix,
            "hypervisor": env.hypervisor,
            "locked": env.locked
        }

        all_envs.append(new_env)
    return json.dumps(all_envs), 200

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    prefix = data['prefix']
    hypervisor = data['hypervisor']

    db.add_instance(envs, prefix=prefix, hypervisor=hypervisor)
    return json.dumps("Added"), 201

@app.route('/remove/<env_id>', methods=['DELETE'])
def remove(env_id):
    db.delete_instance(envs, id=env_id)
    return json.dumps("Deleted"), 204

@app.route('/edit/<env_id>', methods=['PATCH'])
def edit(env_id):
    data = request.get_json()
    new_prefix = data['prefix']
    new_hypervisor = data['hypervisor']
    db.edit_instance(envs, id=env_id, prefix=new_prefix, hypervisor=new_hypervisor)
    return json.dumps("Edited"), 200

@app.route('/lock', methods=['POST'])
def edit(env_id):
    db.edit_instance(envs, id=env_id, locked=True)
    return json.dumps("Locked"), 200
    
@app.route('/release', methods=['POST'])
def edit(env_id):
    db.edit_instance(envs, id=env_id, locked=False)
    return json.dumps("Released"), 200

@app.route('/first_free', methods=['GET'])
def first_free(env_id):
    envs = db.get_all(Environments)
    for env in envs:
        if not env.locked:
            free_env = {
                "id": env.id,
                "prefix": env.prefix,
                "hypervisor": env.hypervisor
            }
    if free_env:
        return json.dumps(free_env), 200
    else:
        return json.dumps("All locked"), 404

if __prefix__ == '__main__':
    app.run()