from temperature_CO2_plotter import plot_temperature
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

# export FLASK_APP=hello.py
# export FLASK_ENV=development
# flask run


@app.route('/')
def root():
    return render_template('form_template.html')


@app.route('/calculate_temperature', methods=['POST'])
def temperature():
    start_year = int(request.form['selectStartYear'])
    end_year = int(request.form['selectEndYear'])
    ymin = float(request.form['ymin'])
    ymax = float(request.form['ymax'])
    month = request.form['selectMonth']

    print(start_year, end_year)
    plot_temperature((start_year, end_year), ymin, ymax, month)

    file = '{}_plot.png'.format(month)

    return render_template('result_template.html',
                           start_year=start_year,
                           end_year=end_year,
                           ymin=ymin,
                           ymax=ymax,
                           month=month,
                           file=file)


# Disables caching to prevent images from not updating, due to being saved in the browser cache
@app.after_request
def disable_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response
