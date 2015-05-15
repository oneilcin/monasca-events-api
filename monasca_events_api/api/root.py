from monasca_events_api.v2.root import V2Controller

import pecan


class RootController(object):
    def __init__(self):
        self._objects = {}
        self._objects['v2.0'] = V2Controller()

    @pecan.expose(content_type="application/json")
    def _lookup(self, key, *remainder):
        if key in self._objects:
            return self._objects[key], remainder

        pecan.abort("404")
