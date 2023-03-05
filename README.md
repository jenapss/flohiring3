# Flask Email Prediction API
This is a Flask API for predicting the category of an email domain using OpenAI's GPT-3 model.

## Requirements
Python 3.x
Flask
OpenAI API key
Installation
Clone the repository: git clone https://github.com/yourusername/flask-email-prediction-api.git
Navigate to the project directory: ```cd flask-email-prediction-api```
Install the required packages: ```pip install -r requirements.txt```
Usage
Run the application: ```python app.py```
Send a GET or POST request to the /prediction/<email> endpoint where email is the domain name you want to predict the category for.


## Example
python
Copy code


```
import requests

url = "http://localhost:5000/prediction/example.com"

response = requests.get(url)

print(response.json())  # {"RESPONSE": "Technology"}
```





