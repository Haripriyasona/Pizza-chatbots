# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/core/customactions/#custom-actions-written-in-python


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
from database import DataUpdate

class Actionname(Action):

    def name(self) -> Text:
         return "action_name"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(template="utter_first_name")

         return [SlotSet('name',tracker.latest_message['text'])]
    DataUpdate(tracker.get_slot("name"))