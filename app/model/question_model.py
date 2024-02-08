from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class Question(db.Model):

    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    questionText = db.Column('questionText', db.String(255), nullable=False)
    choices = db.Column(db.JSON, nullable=False)

    def __init__(self, questionText, choices):
        self.questionText = questionText
        self.choices = choices

    def __repr__(self):
        return '<Question %r>' % self.questionText

    def to_dict(self):
        return {
            'id': self.id,
            'questionText': self.questionText,
            'choices': self.choices
        }

