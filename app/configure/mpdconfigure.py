from flask import flash
from subprocess import call
from config import Config


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
            configfile = "%s/mpd-configure.conf" % Config.MPDCONFIGURE
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
        call('%s/mpd-configure' % Config.MPDCONFIGURE)
        flash('mpd configured. restart and cross your fingers')
        #TODO: Add some error control 

    def apply(self, settings):
        s = settings
        configfile = self.configfile(s)
        self.run_mpdconfigure(configfile)

