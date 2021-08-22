import jimi

class _webTriggerOutput(jimi.db._document):
    webTriggerID = str()
    webTriggerExecutionID = str()
    output_data = str()

    _dbCollection = jimi.db.db["webTriggerOutput"]

    def new(self, acl, webTriggerID, webTriggerExecutionID, output_data):
        self.acl = acl
        self.webTriggerID = webTriggerID
        self.webTriggerExecutionID = webTriggerExecutionID
        self.output_data = output_data
        return super(_webTriggerOutput, self).new()
