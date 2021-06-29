import jimi

class _webTrigger(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        jimi.model.registerModel("webTrigger","_webTrigger","_document","plugins.webTrigger.models.webTrigger",True)
        return True

    def uninstall(self):
        jimi.model.deregisterModel("webTrigger","_webTrigger","_document","plugins.webTrigger.models.webTrigger")
        return True

    def upgrade(self,LatestPluginVersion):
        return True
