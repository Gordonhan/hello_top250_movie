# -*- coding:utf-8 -*-
import random

import config


def get_header():
    config.HEADER['user-agent'] = random.choice(config.USER_AGENTS)
    return config.HEADER
