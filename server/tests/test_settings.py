import atexit
import os
import tempfile

from eventomat.settings import *  # NOQA

tmpdir = tempfile.TemporaryDirectory()
os.environ.setdefault('DATA_DIR', tmpdir.name)

DATA_DIR = tmpdir.name

atexit.register(tmpdir.cleanup)

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True
