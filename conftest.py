"""This conftest script is borrowed from github.com/kevinrockwell"""
import sys
import os

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, root)
