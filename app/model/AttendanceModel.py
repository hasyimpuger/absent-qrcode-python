from app import db
from app.model.StudentModel import Student
import datetime


class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __init__(self, student_id):
        self.student_id = Student.findById(student_id).id

    def __repr__(self):
        return "<Student id: {}>".format(self.student_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getAll():
        data = Attendance.query.all()
        result = list()
        for value in data:
            obj = {
                "id": value.id,
                "student": Student.getById(value.student_id),
                "time": value.time
            }
            result.append(obj)
        return result
