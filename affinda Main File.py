import time
import requests
from flask import Flask, request, jsonify
from pathlib import Path
from os import listdir
from os.path import isfile, join
'''import zipfile
with zipfile.ZipFile('test_resume.zip', 'r') as zip_ref:
    zip_ref.extractall('Test')'''


onlyfiles = [f for f in listdir('Test/test_resume') if isfile(join('Test/test_resume', f))]
print(onlyfiles)
# creating a Flask app
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

@app.route('/home1/', methods=['GET'])
def resume():
    url = "https://api.affinda.com/v1/documents/"
    token = "58a829d345b0e535683d10793ee89f1fa7ae0948"
    headers = {"Authorization": f"Bearer {token}"}

    dic = dict()

    for x in range(0,len(onlyfiles)):
        FILE_TO_UPLOAD_PATH = Path('Test/test_resume/'+onlyfiles[x])
        with open(FILE_TO_UPLOAD_PATH, "rb") as doc_file:
            response = requests.post(
                url,
                data={"fileName": FILE_TO_UPLOAD_PATH.name},
                files={"file": doc_file},
                headers=headers,
            )

        time.sleep(5)
        identifier = response.json()["identifier"]
        name = response.json()["fileName"]
        url1 = f"https://api.affinda.com/v1/documents/{identifier}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url1, headers=headers)
        #dic[identifier] = response.json()
        dic[name] = response.json()
    return dic

if __name__ == '__main__':
    app.run(debug=True)