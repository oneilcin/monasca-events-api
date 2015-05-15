from monasca_events_api.v2.events import Events

import pecan


class V2Controller(object):
    @pecan.expose(content_type="application/json")
    def _lookup(self, key, *remainder):
        if key == "events":
            return Events(), remainder

        pecan.abort("404")
