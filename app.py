# import necessary libraries
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///energysqlite"

db = SQLAlchemy(app)


class 2016-EnergyExpenditure(db.Model):
    __tablename__ = '2016-EnergyExpenditure'

    id = db.Column(db.Integer, primary_key=True)
    state= db.Column(db.String(20))
    btu =  db.Column(db.INTEGER)
    expenditure_per_state = db.Column(db.INTEGER)
    expenditure_per_person_dollars = db.Column(db.INTEGER)
    energyexpenditure_gdp_percent = db.Column(db.INTEGER)
    def __repr__(self):
        return '<(EnergyExpenditure %r>' % (self.expenditure_per_state)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()


#################################################
# Routes
#################################################

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        state = request.form["state"]
        btu = request.form["btu"]
        expenditure_per_state = request.form["expenditure_per_state"]
        expenditure_per_person_dollars = request.form["expenditure_per_person_dollars"]
        energyexpenditure_gdp_percent = request.form["energyexpenditure_gdp_percent"]

        2016-EnergyExpenditure = 2016-EnergyExpenditure(state=state, btu=btu,expenditure_per_state= expenditure_per_state, expenditure_per_person_dollars=expenditure_per_person_dollars,energyexpenditure_gdp_percent=energyexpenditure_gdp_percent )
        db.session.add(EnergyExpenditure)
        db.session.commit()

        return "Thanks for the form data!"

    return render_template("form.html")


@app.route("/2016-EnergyExpenditure")
def list_EnergyExpenditure():
    results = db.session.query(2016-EnergyExpenditure.state, 2016-EnergyExpenditure.btu, 2016-EnergyExpenditure.expenditure_per_state, 2016-EnergyExpenditure.expenditure_per_person_dollars, 2016-EnergyExpenditure.energyexpenditure_gdp_percent).all()

    2016-EnergyExpenditure = []
    for result in results:
        2016-EnergyExpenditure.append({
            "state": result[0],
            "btu": result[1],
            "expenditure_per_state" : result[2],
            "expenditure_per_person_dollars" : result[3],
            "energyexpenditure_gdp_percent" :result[4]
            
        })
    return jsonify(2016-EnergyExpenditure)


@app.route("/")
def home():
    return "Welcome!"

if __name__ == "__main__":
    app.run()
