from flask import Flask, render_template
from routes.home import home_route
from routes.pesquisador import pesquisador_route


app = Flask(__name__)


app.register_blueprint(home_route)
app.register_blueprint(pesquisador_route, url_prefix='/pesquisador')

app.run(debug=True)