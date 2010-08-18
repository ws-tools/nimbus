import sys
import os
import logging
import traceback
from ConfigParser import SafeConfigParser
import hmac
try:
    from hashlib import sha1 as sha
    from hashlib import sha256 as sha256
except ImportError:
    import sha
import base64

Version = "0.1"

def log(level, msg, tb=None):
    logging.log(level, msg)
    if tb != None:
        logging.log(level, "Stack trace")
        logging.log(level, "===========")
        stack = tb.format_exc()
        logging.log(level, stack)
        logging.log(level, "===========")
        logging.log(level, sys.exc_info()[0])


class VConfig(object):

    def __init__(self):
        self.set_defaults()
        if 'NIMBUS_HOME' not in os.environ:
            emsg = "the env NIMBUS_HOME must be set"
            log(logging.WARNING, emsg)
        else:
            ini_file = os.path.join(os.environ['NIMBUS_HOME'], "etc/virga.ini")

            try:
                self.load_settings(ini_file)
            except:
                emsg = "failed to load %s, using defaults" % (ini_file)
                log(logging.WARNING, emsg)
        logging.basicConfig(filename=self.logfile, level=self.log_level)

    def set_defaults(self):
        self.pw = "nimbus"
        self.logfile = "virga.log"
        self.log_level = logging.DEBUG
        self.dbfile = None

    def load_settings(self, ini_file):
        log_levels = {'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL}


        s = SafeConfigParser()
        s.readfp(open(ini_file, "r"))
        self.pw = s.get("security", "password")
        self.logfile = s.get("log", "file")
        try:
            log_level_str = s.get("log", "level")
            self.log_level = log_levels[log_level_str]
        except Exception, ex:
            pass
        try:
            self.dbfile = s.get("db", "file")
        except:
            pass

config = VConfig()

def get_auth_hash(header_str):
    myhmac = hmac.new(config.pw, digestmod=sha)
    header_str = header_str.replace("\n", "")
    header_str = header_str.replace("\r", "")
    myhmac.update(header_str)
    auth_hash = base64.encodestring(myhmac.digest()).strip()
    return auth_hash


