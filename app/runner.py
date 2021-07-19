import datetime

from app.importer import bhacopyimporter
from app.importer.PortfolioImporter import IDirectImporter
from app.ui import CLIMenu
from importer.MasterDataImporter import BSEMasterDataImporter, NSEMasterDataImporter



def main():
    print("Starting Iganit......")
    trade_date = datetime.datetime(2021, 7, 6)
    answers_level0, answers_level1,answers_level2 = CLIMenu.Menu().collectCLInputs()
    print("Your answers :", answers_level0, answers_level1,answers_level2)
    processUserInputs(answers_level0, answers_level1,answers_level2)


def processUserInputs(answers_level0, answers_level1,answers_level2):
    if (answers_level1.get('level1.1_menu') == 'Import NSE MasterData'):
        NSEMasterDataImporter().fetch()
    elif (answers_level1.get('level1.1_menu') == 'Import BSE MasterData'):
        BSEMasterDataImporter().fetch()
    elif (answers_level1.get('level1.1_menu') == 'Import IDirect Portfolio'):
        IDirectImporter().fetch()
    elif(answers_level1.get('level1.1_questions') == 'BhavCopy'):
        if(answers_level2.get('level2.4_questions') == 'BSE'):
            bhacopyimporter.BSEBhavCopyImporter().fetch()
        elif(answers_level2.get('level2.4_questions') == 'NSE'):
            bhacopyimporter.NSEBhavCopyImporter().fetch()



if __name__ == "__main__":
    main()
