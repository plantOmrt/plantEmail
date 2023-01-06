
from flask import Flask, render_template, request
import openai
import flask_mail

## Enter your Open API Key here
openai.api_key = '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'

app = Flask(__name__)


@app.route('/getplant', methods=["GET"])
def coldEmails():

    promptPlant = "write an email as a plant character asking your owner for water in a rude and gangaster way"
    
    query = openAIQuery(promptPlant)
    answer = query["choices"][0]["text"]

    return answer, 200


def openAIQuery(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        temperature=0.8,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)