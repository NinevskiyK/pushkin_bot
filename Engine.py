import markovify
import json

with open('model_json.json') as fl:
    model_json = json.load(fl)
    text_model = markovify.Text.from_json(model_json)

def make_continue_markovify(start):
    start = start.lower()
    try:
        return text_model.make_sentence_with_start(start).replace(' _ ', '\n')
    except:
        return start + ' ' + text_model.make_sentence().replace(' _ ', '\n')

