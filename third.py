

import openai 
import os
def Third(nop):
  openai.api_key = "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"
  print('DALLE being invoked')
  response = openai.Image.create(prompt=nop,n=1,size="1024x1024")
  image_url = response['data'][0]['url']
  return image_url