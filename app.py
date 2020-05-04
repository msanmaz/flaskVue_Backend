import requests
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


def getSearchURL(q,url):
    try:
        import urlparse
        from urllib import urlencode
    except:  # For Python 3
        import urllib.parse as urlparse
        from urllib.parse import urlencode

    params = {'ingredients': q, 'apiKey': '22e3e51a09f1452ead46fcfd2abd5967'}

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)

    return urlparse.urlunparse(url_parts)





@app.route('/search', methods=['GET'])
def dickies():
    url = "https://api.spoonacular.com/recipes/findByIngredients?"
    query = request.args.get('q')
    r = requests.get(getSearchURL(query,url))
    data = r.json()
    return jsonify(data)


@app.route('/recipe/<recipe_id>', methods=['GET'])
def recipeGet(recipe_id):
    url = "https://api.spoonacular.com/recipes/informationBulk?ids="+recipe_id+"&includeNutrition=true"
    query = request.args.get('q')
    r = requests.get(getSearchURL(query,url))
    data = r.json()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
