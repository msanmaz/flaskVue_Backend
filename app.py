import requests,json
from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


def getSearchURL(q):
  try:
      import urlparse
      from urllib import urlencode
  except: # For Python 3
      import urllib.parse as urlparse
      from urllib.parse import urlencode

  url = "https://api.spoonacular.com/recipes/findByIngredients?"
  params = {'ingredients': q, 'apiKey':'f9fffeb9a1fb4e5598bff2b4058ad44f'}

  url_parts = list(urlparse.urlparse(url))
  query = dict(urlparse.parse_qsl(url_parts[4]))
  query.update(params)

  url_parts[4] = urlencode(query)

  return urlparse.urlunparse(url_parts)



@app.route('/recipe', methods=['POST','GET'])
def get_recipe():
    return jsonify('Hello!')

@app.route('/search', methods=['GET'])
def dickies():
    q = request.args.get('q')
    r = requests.get(getSearchURL(q))
    data = r.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run()