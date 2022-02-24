from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)


@app.route('/', methods=['GET'])
def home():
    return 'mencoba API'

# import qrcode
# import base64
# from io import BytesIO
#
# img = qrcode.make('Some data')
# image = img.get_image()
# encoding_64 = base64.b64encode(image)

# with open(image) as to_base_64:
#     encoded = base64.b64encode(to_base_64.read())


# buffered = BytesIO()
# img.save(buffered, format="JPEG")
# img_str = base64.b64encode(buffered.getvalue())
# print('data:image/jpeg;base64,' + str(img_str))
