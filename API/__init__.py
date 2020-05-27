from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from Processing.Filter import Filter
from Processing.Frame import Frame
from Processing.ImageProcessor import ImageProcessor
import datetime

app = Flask(__name__)


#__all__ = [Processing.Filter,]
#TODO Add possibility to save as new name

# Example json post request
# {
# 	"PictureUrl"	  : "https://dl.reseau-ges.fr/public/dcj6AO1JD5-IfaXC28_maGKNp4m2pxjP",
# 	"PictureName"	  : "test",
# 	"Filter"    	  : "GRAYSCALE",
# 	"FilterIntensity" : "0.5",
# 	"ExportFormat"    : "jpg"
# }

#todo add exception handling for images and connection problems
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':


        postJson = request.get_json()


        myFrame = Frame(postJson["PictureUrl"], postJson["PictureName"], postJson["ExportFormat"])
        myFilter = Filter(postJson["Filter"], postJson["FilterIntensity"], postJson["ExportFormat"])

        frameResult = ImageProcessor.applyFilter(myFrame, myFilter)

        #todo add list of pipeline of applied filters 'appliedFilters': [...],
        return jsonify({
            'imageURI': frameResult.NewUrl,
            'creationDate': str(datetime.datetime.now())
        }), 201

        #newPhoto = proc.applyFilter(myPhoto, myFilter)

    else:
        return jsonify({'exception': "something went wrong.."})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)