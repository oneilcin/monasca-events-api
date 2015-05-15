from monasca_events_api.v2.events import Events

import pecan


class V2Controller(object):
    def __init__(self):
        self._objects = {}
        self._objects['events'] = Events()

    @pecan.expose(content_type="application/json")
    def _lookup(self, key, *remainder):
        if key in self._objects:
            return self._objects[key], remainder

        pecan.abort("404")
