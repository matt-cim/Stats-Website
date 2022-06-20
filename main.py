from flask import Flask
from pages import pages

app = Flask(__name__)
# set base tag for pages
app.register_blueprint(pages, url_prefix = "/pages")


#used to start the website
if __name__ == "__main__": app.run(debug = True, port = 5000)