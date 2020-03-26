from app import db

class Task(db.Model):
    __tablename__ = 'tasks'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    priority = db.Column(db.Integer)
    end_date = db.Column(db.String(), default='')
    complete = db.Column(db.Boolean, default=False, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'end_date': self.end_date,
            'complete': self.complete
        }

    def __repr__(self):
        return '<task {}>'.format(self.title)
