from temperature_CO2_plotter import plot_temperature, plot_CO2, plot_CO2_by_country
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

# export FLASK_APP=web_visualization.py
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

    plot_temperature((start_year, end_year), ymin, ymax, month)

    file = '{}_plot.png'.format(month)

    return render_template('result_template.html',
                           start_year=start_year,
                           end_year=end_year,
                           ymin=ymin,
                           ymax=ymax,
                           month=month,
                           file=file)


@app.route('/calculate_co2', methods=['POST'])
def co2():
    start_year = int(request.form['selectStartYearCo2'])
    end_year = int(request.form['selectEndYearCo2'])
    ymin = int(request.form['yminCo2'])
    ymax = int(request.form['ymaxCo2'])

    plot_CO2((start_year, end_year), ymin, ymax)
    file = 'CO2_levels_{}_{}.png'.format(str(start_year), str(end_year))

    return render_template('result_co2_template.html',
                           start_year=start_year,
                           end_year=end_year,
                           ymin=ymin,
                           ymax=ymax,
                           file=file)


@app.route('/calculate_co2_bc', methods=['POST'])
def calculate_co2_bc():
    year = int(request.form['selectCo2Year'])
    threshold = float(request.form['threshold'])

    plot_CO2_by_country(year, threshold)
    file='CO2_levels_{}.png'.format(year)

    return render_template('result_co2_bc_template.html',
                           year=year,
                           threshold=threshold,
                           file=file)


@app.route('/help')
def helper():
    return render_template('temperature_CO2_plotter.html')

# Disables caching to prevent images from not updating, due to being saved in the browser cache
@app.after_request
def disable_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response
