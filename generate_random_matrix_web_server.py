#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   request,
                   flash)
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  if request.method == 'POST':
    try:
      try:
        int(request.form['matrix_rows'])
        int(request.form['matrix_columns'])
      except Exception as e:
        raise e
      try:
        float(request.form['max_random_value'])
      except Exception as e:
        raise RuntimeError('Please provide a number '
                           'for the max random value.')
      flash('Matrix parameters: Rows = {}, '
            'Columns = {}, '
            'Max random value = {}'
            .format(request.form['matrix_rows'],
                    request.form['matrix_columns'],
                    request.form['max_random_value']))
      return render_template('index.html')
    except Exception as e:
      flash(e)
      return render_template('index.html')
