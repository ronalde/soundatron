from flask import render_template, flash
from . import configure
from .forms import WizardSettings
from .mpdconfigure import MpdConfigure

mpd = MpdConfigure()


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardSettings()
    if form.validate_on_submit():
        settings = {'DEBUG': 'True'}
        settings['prefferedfilter'] = form.prefferedfilter.data
        settings['enablezeroconf'] = form.enablezeroconf.data
        settings['zeroconfname'] = form.zeroconfname.data
        flash(settings)
        mpd.apply(settings)

    return render_template('wizard.html', form=form)
