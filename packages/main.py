#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging.config
import yaml

if __name__ == "__main__":
  
    def setup_logging(
        default_path='logging.yaml',
        default_level=logging.INFO,
        env_key='LOG_CFG'
    ):
        """Setup logging configuration

        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.safe_load(f.read())
                """print(config["handlers"])
                exit()"""
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            
    setup_logging(default_path=os.path.join(os.path.dirname(__file__), "..", "..", "conf/logging.yaml"))

    logging = logging.getLogger("debuger")

    logging.debug('This is a debug')
    logging.info('This is a info')
    logging.warning('This is a warning')
    logging.error('This is a error')
    logging.critical('This is a critical')
    
    exit()
