from app import db


class Student(db.Model):
    __tablename__ = "student"  # Must be defined the table name

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    nim = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    qr_code = db.Column(db.String, nullable=False, unique=True)
    attendance = db.relationship("Attendance", backref="student", lazy="dynamic")

    def __init__(self, nim, name, qr_code):
        self.nim = nim
        self.name = name
        self.qr_code = qr_code

    def __repr__(self):
        return "<Name: {}, Nim: {}>".format(self.name, self.nim)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getAll():
        students = Student.query.all()
        result = []
        for student in students:
            obj = {
                "id": student.id,
                "nim": student.nim,
                "name": student.name,
                "qr_code": student.qr_code
            }
            result.append(obj)
        return result

    @staticmethod
    def getById(id):
        student = Student.findById(id)
        result = {
            "id": student.id,
            "nim": student.nim,
            "name": student.name,
            "qr_code": student.qr_code
        }
        return result

    @staticmethod
    def findById(id):
        return Student.query.filter_by(id=id).first()
