#!/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from server import MyClient

if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = MyClient(token)
    client.run(token)