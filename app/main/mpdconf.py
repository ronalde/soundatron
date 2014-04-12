from config import basedir


def mpdconf_maker(self, **kwargs):
    import ipdb; ipdb.set_trace()
    if kwargs is not None:
        conffile = "%s/mpd-configure.conf" % basedir
        f = open(conffile, 'w')
        for key, value in kwargs.iteritems():
            f.write("%s=%s\n" % (key, value))
        f.close()
