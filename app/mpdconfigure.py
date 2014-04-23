# -*- encoding:utf-8 -*-
from flask import flash, current_app
import subprocess


class MpdConfigure(object):
    """
    Create, and apply mpd conf files using mpd-configure
    https://github.com/ronalde/mpd-configure
    """

    def configfile(self, settings):
        """
        Take user input settings and create mpd-configure conf file
        """

        if settings is not None:
            configfile = "%s/mpd-configure.conf" % \
                current_app.config['MPDCONFIGURE']
            f = open(configfile, 'w')
            for key, value in settings.iteritems():
                f.write("%s=%s\n" % (key, value))
            f.close()
            return configfile
        else:
            pass
        # TODO: add an error

    def run_mpdconfigure(self, file):
        """
        Apply settings in mpd-configure conf file"
        """
        flash(file)
        subprocess.call('%s/mpd-configure' % current_app.config['MPDCONFIGURE'])
        flash('mpd configured. restart and cross your fingers')
        #TODO: Add some error control

    def stopmpd(self):
        # This doesn't work ... no permisions
        subprocess.call(["service", "mpd", "stop"])

    def startmpd(self):
        # This doesn't work ... no permisions

        subprocess.call(["service", "mpd", "start"])

    def apply(self, settings):
        s = settings
        configfile = self.configfile(s)
        self.run_mpdconfigure(configfile)
