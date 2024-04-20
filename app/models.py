from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
    due_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"