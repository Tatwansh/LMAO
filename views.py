from flask import render_template, flash
from app import app


# Route Decorators
@app.route("/")
def index():
    return render_template("index.html")


#####Custom Error Page
# Invalid URL
@app.errorhandler(404)
def the4o4(e):
    return render_template("4o4.html"), 404


# InternalServerError
@app.errorhandler(500)
def the5oo(e):
    return render_template("5oo.html"), 500


###### Creation of a webForm
@app.route("/details", methods=['GET', 'POST'])
def webForm():
    fname = ""
    lname = ""
    form = WForm()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        form.fname.data = ''
        form.lname.data = ""
        flash("Details entered successfully!")

    return render_template("details.html", fname=fname, lname=lname, form=form)