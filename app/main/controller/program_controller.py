from ..service.program_service import setProgram, getPrograms

def savePrograms(form):
    dataDict = {
            'name': form['name'],
            'description': form['description'],
        }
    return setProgram(data=dataDict)

def listPrograms():
    return getPrograms()