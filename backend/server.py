from flask import (Flask, render_template, request, flash,
                    redirect)
from model import connect_to_db, db
import crud

app = Flask(__name__)


app.secret_key = 'Secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db.init_app(app)

@app.route('/')
def home():
    """Display the homepage"""
    pass
   

if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
     )
    


# TO-DO, get a homepage to display 