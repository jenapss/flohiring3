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
  
  
  
## Continuous Integration and Continuous Deployment (CI/CD)
This project uses GitHub Actions to implement a CI/CD pipeline to automatically build and deploy changes to Elastic Beanstalk whenever changes are pushed to the main branch.

## CI Pipeline
When changes are pushed to the main branch, the CI pipeline will be triggered. The pipeline consists of the following steps:

Checkout source code from GitHub repository.
Generate deployment package using zip.
Configure AWS credentials.
Copy the deployment package to an S3 bucket.
Finish the CI pipeline.
CD Pipeline
The CD pipeline is triggered by the completion of the CI pipeline. The pipeline consists of the following steps:

## Configure AWS credentials.
Create a new Elastic Beanstalk application version.
Deploy the new application version to the Elastic Beanstalk environment.
Print a message indicating that the deployment was successful.

## Secrets
To implement the CI/CD pipeline, we need to configure two secrets in our repository settings:

AWS_ACCESS_KEY_ID: The access key ID for an AWS account with permissions to access Elastic Beanstalk and S3.
AWS_SECRET_ACCESS_KEY: The secret access key for the same AWS account.
License
This project is licensed under the MIT License. See the LICENSE file for more information.









