#!/opt/raindrop/venv/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/opt/raindrop/')
from raindrop import app as application

