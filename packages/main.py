#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
install: pip install flake8 / pip install flake8-colors / 
HTML: flake8 testflake8.py --format=html --htmldir=flake-report
usage: flake8 / flake8 bootcamp/feeds/
Configuring: setup.cfg / https://flake8.pycqa 
dqsdqsdqdqdsqdsdqdqdsfsdfsdfsdffsdfsdfsdffdsdff



[flake8]
exclude = .git,*migrations*
max-line-length = 119 


// PRE COMMIT

pip install pre-commit
pre-commit install # dans le projet
SKIP=flake8 git commit -m "foo"
"""

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
