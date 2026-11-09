
# Copyright (c) 2021 - Present partiallywritten
# Author: https://github.com/partiallywritten
# Project: https://github.com/partiallywritten/Mega.nz-Bot

import os
import logging

# Start message
print("Mega.nz Bot - Cypher is starting...")

# Loading config
from dotenv import load_dotenv

print("--------------------")
print("> Loading config")

if os.path.isfile(".env"):
    load_dotenv()
else:
    logging.warning("WARNING: No .env file found")

# Client
from .helpers.cypher import MeganzClient

CypherClient: "MeganzClient" = MeganzClient()
