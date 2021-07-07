# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.forms import FormAction, REQUESTED_SLOT


class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "admission_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("required_slots(tracker: Tracker)")
        return ["name", "ssn", "subject"]    

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(response="utter_submit")

        return []
