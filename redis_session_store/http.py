# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

import odoo

from odoo.tools.func import lazy_property
from odoo.http import OpenERPSession
from odoo.tools import config
from sessionstore import RedisSessionStore
from werkzeug.contrib.sessions import FilesystemSessionStore
import redis


class CustomRoot(odoo.http.Root):
    @lazy_property
    def session_store(self):
        # if redis enabled in config, use him as session store
        if config.get('use_redis', False):
            logger.debug("HTTP sessions stored in Redis")

            redis_host = config.get('redis_host', 'localhost')
            redis_port = config.get('redis_port', 6379)
            redis_salt = config.get(
                'redis_salt',
                '-RMsSz~]3}4[Bu3_aEFx.5[57O^vH?`{X4R)Y3<Grvq6E:L?6#aoA@|/^^ky@%TI'
            )

            logger.debug("Connecting Redis at {}:{}".format(redis_host, redis_port))
            redis_instance = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
            return RedisSessionStore(redis_instance, redis_salt, session_class=OpenERPSession)

        path = config.session_dir
        logger.debug('HTTP sessions stored in: %s', path)
        return FilesystemSessionStore(path, session_class=OpenERPSession)


root = CustomRoot()
odoo.http.root.session_store = root.session_store
