from nbconvert.exporters import Exporter


class DummyExporter(Exporter):
    pass


class DummyScriptExporter(Exporter):
    def from_notebook_node(self, nb, resources=None, **kw):
        return "dummy-script-exported", resources
