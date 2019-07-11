import json
import requests

# Return json Builders------------------------------------------------------------------------------

def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech

def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response

def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card

def statement(title, body, b):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = b
    return build_response(speechlet)


# intent functions-----------------------------------------------------------------------------


def kiddiet(event, context):
    diet = "A healthy, balanced diet for children aged 7 to 10 should include: at least 5 portions of a variety of fruit and vegetables every day. meals based on starchy foods, such as potatoes, bread, pasta and rice (choose wholegrain varieties when possible) some milk and dairy products suggested choose low-fat options where you can"
    return statement("getting_kiddiet",diet, False)



def kidplay(event, context):
    play="kids play options would be ludo,sudoco,snake n ladder,chess,morris,badminton"
    return statement("getting_kidplay",play, False)


def kidjokes(event, context):
    joke="Why was 6 afraid of 7? Because 7, 8, 9"
    return statement("getting_kidjoke",joke, False)

def kidsnickname(event,context):
    v= event['request']['intent']['slots']['nick']['value']
    s="hi "+v+" you got a very good nickname"
    return statement("nickname",s, False)

# ---------------------------------------------------------------Identifying intents
def intent_router(event, context):
    intent = event['request']['intent']['name']

    if intent == "kiddiet":
        return kiddiet(event, context)

    if intent == "kidplay":
        return kidplay(event, context)       

    if intent == "kidjokes":
        return kidjokes(event, context) 

    if intent == "kidsnickname":
        return kidsnickname(event, context)  

    if intent == "AMAZON.StopIntent":
        return statement("stop","it was nice talking to u see u again",True)
# ----------------------------------------------------------------Welcome message
def on_launch(event, context):
    return statement("hello","Welcome to kids treasure", False)


#------------------------------------------------------------------Opening short news 
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)
