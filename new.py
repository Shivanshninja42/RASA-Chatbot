
import os
import openai

import requests

def New(user_input):

    openai.api_key = "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"

    # city=input('messages')
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system","content":user_input}],
  
    )
    response_text = response['choices'][0]['message']['content']

    return response_text
