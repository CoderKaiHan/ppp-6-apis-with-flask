from flask import ( Blueprint, render_template, request, jsonify)

from ..models import models


#code learning for each step refer to project "petfax"
bp= Blueprint(
    'reptile',
    __name__,
    url_prefix='/reptiles',
)


@bp.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientificf_name = request.form['scientificf_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_facts = request.form['fun_facts'],
        )
        models.db.session.add(reptile)
        models.db.session.commit()


    reptiles = models.Reptile.query.all()
    # Return JSON response
    return jsonify([reptile.to_json() for reptile in reptiles])



@bp.route('/<int:id>')
def detail(id):
    reptile = models.Reptile.query.get(id)
    return jsonify(reptile.to_json())