from flask import Flask
import tweepy

from Controllers.Dashboard import Dashboard as dash

app = Flask(__name__)

@app.route('/')
def test():
    return dash.index()

if __name__=="__main__":
    app.run(debug=True)