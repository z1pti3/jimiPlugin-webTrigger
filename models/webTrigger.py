import secrets

import jimi

class _webTriggerEvent(jimi.db._document):
    webTriggerID = str()
    formResult = dict()
    runTime = int()
    webTriggerExecutionID = str()

    _dbCollection = jimi.db.db["webTriggerEvent"]

    def new(self, acl, webTriggerID, formResult):
        self.acl = acl
        self.webTriggerID = webTriggerID
        self.formResult = formResult
        self.webTriggerExecutionID = secrets.token_hex(128)
        super(_webTriggerEvent, self).new()
        return self.webTriggerExecutionID

class _webTriggerOutput(jimi.db._document):
    webTriggerID = str()
    webTriggerExecutionID = str()
    outputData = str()

    _dbCollection = jimi.db.db["webTriggerOutput"]

    def new(self, acl, webTriggerID, webTriggerExecutionID, outputData):
        self.acl = acl
        self.webTriggerID = webTriggerID
        self.webTriggerExecutionID = webTriggerExecutionID
        self.outputData = outputData
        return super(_webTriggerOutput, self).new()
