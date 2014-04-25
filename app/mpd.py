# -*- encoding:utf-8 -*-
from signal import signal, SIGPIPE, SIG_DFL
import subprocess
import os
import re


def availableinterfaces():
    script = os.path.join('scripts', 'mpd-configure', 'examples',
                          'get-interfaces-for-python.sh')
    aiflines = subprocess.check_output(script, shell=True, preexec_fn=lambda:signal(SIGPIPE, SIG_DFL)).splitlines()
    aiflist = []

    for line in aiflines:
        aifline = re.split(r'[()]', line)
        label = aifline[0]
        idx = aifline[1]
        aiflist.append((idx, label))
    return aiflist


def applysettings(settings):
    """
    Applies mpd settings dictionary
    """
    script = os.path.join('scripts', 'mpd-configure', 'mpd-configure')
    configfile = os.path.join('scripts', 'mpd-configure', 'mpd-configure.conf')
    f = open(configfile, 'w')
    for key, value in settings.iteritems():
        f.write("%s=%s\n" % (key, value))
    f.close()
    subprocess.call(script)

