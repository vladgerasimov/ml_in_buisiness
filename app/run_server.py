import os
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
from model import Model

app = flask.Flask(__name__)
model = Model()

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    images = None
    if flask.request.method == "POST":
        request_json = flask.request.get_json()
        if request_json:
            images = request_json
        logger.info(f'{dt} Images_number = {len(images)}')
        try:
            preds = model.get_predictions(images)
        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            return flask.jsonify(data)
        data["predictions"] = preds
        data["success"] = True
    print(preds)
    return flask.jsonify(data)


if __name__ == "__main__":
    print("* Loading the model and Flask starting server...", "please wait until server has fully started")
    port = int(os.environ.get('PORT', 8181))
    app.run(host='0.0.0.0', debug=True, port=port)
