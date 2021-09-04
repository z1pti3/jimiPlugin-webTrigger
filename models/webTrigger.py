import uuid

import jimi

class _webTriggerEvent(jimi.db._document):
    webTriggerID = str()
    formResult = dict()
    runTime = int()
    webTriggerExecutionID = str()

    _dbCollection = jimi.db.db["webTriggerEvent"]

    def new(self, acl, webTriggerID, fromData):
        self.acl = acl
        self.webTriggerID = webTriggerID
        self.fromData = fromData
        self.webTriggerExecutionID = str(uuid.uuid4())
        return super(_webTriggerEvent, self).new()

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
