from rasa_sdk import Action

class ActionPegaCorpoEmail(Action):

    def name(self):
        return "action_pega_corpo_email"

    def run(self, dispatcher, tracker, domain):
        print("Teste")
        dispatcher.utter_message("Hello World!")

        return []
