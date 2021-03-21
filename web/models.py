import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Environments(db.Model):
    __tableprefix__ = "environments"
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(30))
    hypervisor = db.Column(db.String(120))
    locked = db.Column(db.Boolean())

    def __init__(self, prefix, hypervisor):
        self.prefix = prefix
        self.hypervisor = hypervisor
        self.locked=False

    def __repr__(self):
        return '<Domain prefix: %r, Hypervisor: %r, Locked: %r>' % (self.prefix, self.hypervisor, self.locked)
