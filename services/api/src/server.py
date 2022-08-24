from flask import Flask, Blueprint, jsonify
from core.auth import authenticate


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

blueprint = Blueprint(
  'root-routes',
  __name__
)

@blueprint.route('/')
def root():
  response = {
    'ok': True,
    'app': authenticate()
  }

  return jsonify(response)

app.register_blueprint(blueprint)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
