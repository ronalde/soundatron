# -*- encoding:utf-8 -*-
from subprocess import Popen, PIPE, STDOUT, check_output
from signal import signal, SIGPIPE, SIG_DFL
import os
import psutil
import shlex


def availableinterfaces():
    aiflines = check_output("aplay -l | grep ^card", shell=True,
                            preexec_fn=lambda: signal(SIGPIPE, SIG_DFL)).splitlines()
    aiflist = []
    for line in aiflines:
        if len(line) > 0:
            label = line
            value = line.split('[', )[2].split(']')[0]
            aiflist.append((value, label))
        else:
            pass
    return aiflist


def runsudocmd(cmd, password):
    """
    Run a regular command as sudo
    """
    sudocmd = ['sudo', '-p', '', '-k', '-S'] + shlex.split(cmd)
    proc = Popen(sudocmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    proc.communicate(input='{0}\n'.format(password))[0]
    return proc.returncode


def pidofmpd():
    pid = [p.pid for p in psutil.process_iter() if "mpd" in str(p.name)]
    if len(pid) > 0:
        pid = pid[0]
        return pid
    else:
        return False


def createconfs(settingsdict):
    """
    Create mpd-configure.conf and mpd.conf file from a dictionary of
    settings used by mpd-configure. See https://github.com/ronalde/mpd-configure
    """
    mpdconfigure = os.path.join('scripts', 'mpd-configure', 'mpd-configure')
    mpdconfigureconf = os.path.join('scripts', 'mpd-configure',
                                    'mpd-configure.conf')
    mpdconf = os.path.join('scripts', 'mpd-configure', 'mpd.conf')
    settings = settingsdict
    settings['MPD_CONFFILE'] = mpdconf

    # Write settings to mpd-configure.conf
    f = open(mpdconfigureconf, 'w')
    f.write('DEBUG=True\n')
    for key, value in settings.iteritems():
        f.write('{0}="{1}"\n'.format(key, value))
    f.close()

    # Create mpd.conf
    Popen(mpdconfigure)

    return mpdconf


def applympdconf(settings, password):
    """
    copy mpd.conf to /etc/mpd.conf and restart mpd server
    """
    conffile = createconfs(settings)
    Popen(['sudo', '-K'])
    runsudocmd('/etc/init.d/mpd stop', password)
    pid = pidofmpd()
    if pid:
        killmpdcmd = 'kill -9 {0}'.format(pid)
        runsudocmd(killmpdcmd, password)
    copycmd = 'cp {0} /etc/mpd.conf'.format(conffile)
    runsudocmd(copycmd, password)
    runsudocmd('/etc/init.d/mpd start', password)
    Popen(['sudo', '-K'])
