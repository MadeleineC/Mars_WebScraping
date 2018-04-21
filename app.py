
# coding: utf-8

# In[3]:


from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars


# In[4]:
app = Flask(__name__, static_url_path='')

mongo = PyMongo(app)

# In[5]:
# @app.route('/scrape')

@app.route('/')
def index():
    mars_db = mongo.db.mars_db.find_one()
    print(mars_db)
    return render_template('index.html', mars_db=mars_db)


@app.route('/scrape')
def scrape():
    mars_db = mongo.db.mars_db
    data = scrape_mars.scrape()
    mars_db.update(
        {},
        data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

#prevent browser from caching 
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)

