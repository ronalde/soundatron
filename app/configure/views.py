from flask import render_template, flash
from . import configure
from .forms import WizardSettings


def mpdconf_maker(settings):
    if settings is not None:
        conffile = "/tmp/mpd-configure.conf"
        f = open(conffile, 'w')
        for key, value in settings.iteritems():
            f.write("%s=%s\n" % (key, value))
        f.close()


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardSettings()
    if form.validate_on_submit():
        settings = {}
        settings['prefferedfilter'] = form.prefferedfilter.data
        settings['enablezeroconf'] = form.enablezeroconf.data
        settings['zeroconfname'] = form.zeroconfname.data
        flash(settings)
        mpdconf_maker(settings)
    return render_template('wizard.html', form=form)
