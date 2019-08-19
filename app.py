from flask import Flask, render_template
import tweepy

from Controllers.Dashboard import Dashboard as dash

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/word_cloud')
def word_cloud():
    return dash.word_cloud()

@app.route('/sentiment')
def sentiment():
    return dash.sentiment()

if __name__=="__main__":
    app.run(debug=True)
    # app.run()