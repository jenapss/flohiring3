from flask import Flask, jsonify

import requests

application = Flask(__name__)

@application.route("/")
def index():
    return "THE application IS UP AND RUNNING!"

@application.route("/prediction/<email>", methods=['POST', "GET"])
def prediction(email):
    
    x = requests.get('http://dev.flohiring.com/candidates/email-domain-headers/{}'.format(email))
    #print('HEADERS',x.json()['headers'])
    #print(type(x.json()['headers']))

    if len(x.json()['headers']) != 0:
        try:
            import openai
            openai.api_key = "xxxxxxxxx"
            ft_model = 'babbage:ft-flohiring-2022-06-15-18-49-16'
            prompt_text = ' '.join(x.json()['headers']) + "\n\n###\n\n"
            print("TTTT", prompt_text)
            # string1= "LATEST NEWS We value rigorous inquiry WE FOSTER INDEPENDENT THINKING Transformative education Field-defining research WE ADVANCE IDEAS AND HUMANITY Intellectual freedom Community impact Global impact We call Chicago home ->"
            res = openai.Completion.create(model=ft_model, prompt=prompt_text, temperature=0,
            max_tokens=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"])
            
            #print("RESPONSE", res['choices'][0]['text'])
            return jsonify({"RESPONSE" : res['choices'][0]['text']})
        except Exception as err:
            return jsonify({"RESPONSE" : "COULD NOT CLASSIFY, MORE TRAINING DATA NEEDED"})
    else:
        return jsonify({"RESPONSE" : 'NO SCRAPING RESULTS'})

    
    
    

if __name__ == "__main__":
    application.run(debug=True)
