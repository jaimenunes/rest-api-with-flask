"""
blocklist.py

this file just contains the blocklist of jwt tokens, it will be impoted by app and logout resource so that tokens can
be add to the blocklist when user logs out
"""

BLOCKLIST = set()