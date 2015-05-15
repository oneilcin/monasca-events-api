from monasca_events_api.v2.root import V2Controller

import pecan


class RootController(object):
    @pecan.expose(content_type="application/json")
    def _lookup(self, key, *remainder):
        if key == "v2.0":
            return V2Controller(), remainder

        pecan.abort("404")
