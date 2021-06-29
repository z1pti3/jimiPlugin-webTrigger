import jimi

class _webTrigger(jimi.db._document):
    name = str()
    description = str()
    icon = str()
    trigger_id = str()
    playbook_id = str()

    _dbCollection = jimi.db.db["webTrigger"]
