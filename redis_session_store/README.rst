Redis session storage for Odoo
=================

This module is fork `<https://github.com/keerati/odoo-redis>` for odoo 10 support.

Module for transfer session store to redis from filesystem.

Configuration
-----------------

1. Append module to odoo *addons_path*;
2. Add parameters to configuration file (odoo.conf):
    - *use_redis (required)*: to enable redis session store
    - *redis_host (optional)*: default to 'localhost'
    - *redis_port (optional)*: default to 6379
    - *redis_salt (optional)*: salt using with generate_key 
3. Restart odoo server
