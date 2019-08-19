from flask import Flask, render_template
import tweepy

from Controllers.Dashboard import Dashboard as dash

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/word_cloud')
def data():
    return dash.index()

if __name__=="__main__":
    app.run(debug=True)
    # app.run()