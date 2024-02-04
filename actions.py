# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests
from typing import Any,Text,Dict,List
from rasa_sdk import Action, Tracker 
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher 
import os
import openai
import requests
from sanic.response import json
from  new import  *
from  second import  *
from weather import *
from  third import  *

class ActionWeatherApi(Action):
    def name(self) -> Text :
        return "action_weather_api"


    def run(self,dispatcher : CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) ->List[Dict[Text,Any]] :
  
     city=tracker.latest_message['text']
     print('Weather API Call')
     temp=int(Weather(city)['temp']-273)
     dispatcher.utter_message(template="utter_temp",temp=temp)
    
     return [] 
    

class NewAction(Action):
    def name(self) -> Text:
        return "new_action"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message=tracker.latest_message.get('text')
        response= New(user_message)
        # dispatcher.utter_message("utter_info",tracker,custom_action=response)
        dispatcher.utter_message(template="utter_info", new_action=response)

        return []
    
class CustomAction(Action):
     def name(self) -> Text:
        
         return "custom_action"

     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
         user_message=tracker.latest_message.get('text')
        
         response= Second(user_message)
         dispatcher.utter_message(template="utter_old",custom_action=response)
         return []
    
class MyAction(Action):
    def name(self) -> Text:       
         return "my_action"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print('DALLE going to be invoked')
         user_message=tracker.latest_message.get('text')        
         response= Third(user_message)
         #dispatcher.utter_message("utter_info",tracker,custom_action=response)
         dispatcher.utter_message(template="utter_picture",my_action=response)
         return []






import os
import openai
import requests
from sanic.response import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from  fourth import  *

class CustomAction(Action):
    def name(self) -> Text:
        return "best_action"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message=tracker.latest_message.get('text')
        response= Fourth(user_message)
    
        dispatcher.utter_message(template="utter_answers", best_action=response)

        return []