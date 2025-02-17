# test/__init__.py
import sys
import os

# Add the parent directory of 'src' to the sys.path to make it accessible
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
