from flask import Flask ,render_template
from flask_bootstrap import Bootstrap
import requests
import json


import requests

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"


headers = {
	"X-RapidAPI-Key": "e4bf63e118msh30082d69a9adae6p17471cjsnd4fbe6b0aa2b",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)



recovered = response.json()["data"]["recovered"]
print(recovered)





app = Flask(__name__)
app.config["SECRET_KEY"] = "DSLKJGDLFKGNSLDSKMHVBDFHBMkdsgj"
Bootstrap(app)


@app.route('/')
def index():
    date = response.json()["data"]["date"]
    deaths = response.json()["data"]["deaths"]
    confirmed_cases= response.json()["data"]["confirmed"]
    fatality_rate = response.json()["data"]["fatality_rate"]
    return render_template("index.html" , **locals())


if __name__ == "__main__":
    app.run(debug=True, port=5752)