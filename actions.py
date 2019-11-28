from rasa_sdk import Action
import json
from rasa_sdk.events import SlotSet

class ActionMontaResCoordenador(Action):

    def name(self):
        return "action_monta_res_coordenador"

    def run(self, dispatcher, tracker, domain):
        res      = {}
        contents = {}

        contents['destiny'] = 'coordenacao'
        contents['content'] = tracker.latest_message['text']

        res['message'] = 'encaminhei o seu email, muito obrigado'
        res['status'] = 1
        res['action'] = 'email'        
        res['contents'] = contents

        print(json.dumps(res))
        return [SlotSet('res_corpo_email', json.dumps(res))]

class ActionMontaResProfessor(Action):

    def name(self):
        return "action_monta_res_professor"

    def run(self, dispatcher, tracker, domain):
        disciplina = tracker.get_slot('disciplina')
        ed = ['estrut', 'ED', 'dados', 'eD', 'Ed', 'ed']
        so = ['sistema', 'operaci', 'SO', 'so', 'So', 'sO']

        ehED = False
        ehSO = False

        for i in ed:
            if(i in disciplina):
                ehEd = True
        
        for i in so:
            if(i in disciplina):
                ehSO = True
        
        if(ehEd):
            disciplina = 'estrutura_de_dados'
        
        elif(ehSO):
            disciplina = 'sistemas_operacionais'
        else:
            disciplina = None

        res      = {}
        contents = {}               

        if(not disciplina):
            contents['destiny'] = ''
            contents['content'] = ''  

            res['message'] = 'Desculpe, não consegui achar sua disciplina'
            res['status'] = 1
            res['action'] = ''        
            res['contents'] = contents
            
        else:
            contents['destiny'] = tracker.get_slot('disciplina')
            contents['content'] = tracker.latest_message['text']

            res['message'] = 'encaminhei o seu email, muito obrigado'
            res['status'] = 1
            res['action'] = 'email'        
            res['contents'] = contents

        print(json.dumps(res))
        return [SlotSet('res_corpo_email', json.dumps(res))]

class ActionMediaDisciplina(Action):

    def name(self):
        return "action_media_disciplina"

    def run(self, dispatcher, tracker, domain):
        res      = {}
        contents = {}
        
        contents['disciplina'] = tracker.get_slot('disciplina')

        res['message']  = 'Sua média para a disciplina ' + tracker.get_slot('disciplina') + ' foi '
        res['status']   = 1
        res['action']   = 'media'        
        res['contents'] = contents

        print(json.dumps(res))
        return [SlotSet('disciplina', json.dumps(res))]

class ActionDataProva(Action):

    def name(self):
        return "action_data_prova"

    def run(self, dispatcher, tracker, domain):
        res      = {}
        contents = {}
        

        res['message']  = 'Segue a data das suas provas: '
        res['status']   = 1
        res['action']   = 'data'        
        res['contents'] = contents

        print(json.dumps(res))
        return [SlotSet('data_prova', json.dumps(res))]