# Server Specific Configurations
server = {
    'port': '8082',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'monasca_events_api.api.launch',
    'modules': ['monasca_events_api'],
    'debug': True,
}
