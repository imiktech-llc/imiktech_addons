Redis session storage for Odoo
=================

This module is fork `<https://github.com/keerati/odoo-redis>` for odoo 10 support.

Module for transfer session store to redis from filesystem.

Configuration
-----------------

1. Install this module.
2. Add parameters to configuration file (odoo.conf):
    + use_redis_session_store (required) : to enable redis session store
    + redis_host (optional) : default to 'localhost'
    + redis_port (optional) : default to 6379
    + redis_salt (optional) : salt using with generate_key 
