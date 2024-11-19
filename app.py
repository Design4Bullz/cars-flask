from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/vehicle'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Car model to match the database structure
class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    color = db.Column(db.String(20))
    price = db.Column(db.Numeric)

    def __repr__(self):
        return f"{self.make} {self.model} ({self.year})"

@app.route('/')
def index():
    cars = Car.query.all()  # Get all cars from the database
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
