from PyInquirer import prompt, print_json


class Menu:

    def collectCLInputs(self):
        topLevel_questions = [
            {
                'type': 'list',
                'name': 'level0_questions',
                'message': 'Choose from the following',
                'choices': ['Import', 'Menu2']
            }
        ]
        import_options = [
            {
                'type': 'list',
                'name': 'level1.1_questions',
                'message': 'Choose from following',
                'choices': ['Import NSE MasterData','Import BSE MasterData','Import IDirect Portfolio','BhavCopy']
            }
        ]
        bhavcopy_options=[
            {
                'type': 'list',
                'name': 'level2.4_questions',
                "message" : 'Please choose Exchange',
                'choices' : ['NSE','BSE']
            }
        ]

        answers_level0 = prompt(topLevel_questions)
        print("Answer0 :", answers_level0)
        if answers_level0.get('level0_questions') == 'Import':
            answers_level1 = prompt(import_options)
            if answers_level1.get('level1.1_questions') == 'BhavCopy':
                answers_level2 = prompt(bhavcopy_options)

        return answers_level0, answers_level1,answers_level2
