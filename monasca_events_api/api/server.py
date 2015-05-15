# Copyright 2015 Hewlett-Packard
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os
from wsgiref import simple_server

from oslo.config import cfg
import paste.deploy

import pecan

from monasca_events_api.openstack.common import log

dispatcher_opts = [cfg.StrOpt('stream_definitions', default=None,
                              help='Stream definition endpoint'),
                   cfg.StrOpt('events', default=None,
                              help='Events endpoint'),
                   cfg.StrOpt('transforms', default=None,
                              help='Transforms endpoint')]

dispatcher_group = cfg.OptGroup(name='dispatcher', title='dispatcher')
cfg.CONF.register_group(dispatcher_group)
cfg.CONF.register_opts(dispatcher_opts, dispatcher_group)

LOG = log.getLogger(__name__)


def launch(conf, config_file="/etc/monasca/events_api.conf"):
    cfg.CONF(args=[],
             project='monasca_events_api',
             default_config_files=[config_file])
    log_levels = (cfg.CONF.default_log_levels)
    cfg.set_defaults(log.log_opts, default_log_levels=log_levels)
    log.setup('monasca_events_api')

    app = pecan.make_app("monasca_events_api.api.root.RootController")

    return app


if __name__ == '__main__':
    wsgi_app = (
        paste.deploy.loadapp('config:etc/events_api.ini',
                             relative_to=os.getcwd()))
    httpd = simple_server.make_server('127.0.0.1', 8082, wsgi_app)
    httpd.serve_forever()
