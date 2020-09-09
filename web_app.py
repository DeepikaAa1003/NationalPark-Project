# TODO Import Statements


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

# TODO DB Configuration

#################################################
# Flask Routes
#################################################

# Homepage
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")

# Park page for selected search result
@app.route('/park/<parkname>')
def park(parkname):
    # TODO logic for rendering the park page using returned data from the parkdb route
    # from mongo_app.py which is run when user selects a parkname link on any page

    return render_template("park.html")

# dashboard page (trying to set up to use default region of 'south' if no region variable is passed in)
@app.route('/dash')
@app.route('/dash/<region>')
def regionaldash(region ='south'):
    # TODO logic for rendering dashboard based on region variable or default value of 'south'


    return render_template('super_awesone_dashboard.html')

# dashboard page based on nearby to a specified park as opposed to region
# (generally the same dash but with different logic for selecting nearby parks)
@app.route('/dash/<parkname>')
def localdash(parkname):
    # TODO logic for rendering dashboard based on parkname variable
    # (should otherwise be similar to regionaldash but with other parks selected by proximity to parkname park)
    return render_template('super_awesone_dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)
