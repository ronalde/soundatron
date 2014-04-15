# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, flash
from .forms import WizardSettings
from .mpdconfigure import MpdConfigure

configure = Blueprint('configure', __name__)
mpd = MpdConfigure()


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardSettings()
    if form.validate_on_submit():
        settings = {'DEBUG': 'True', 'DRYRUN': 'True'}
        settings['prefferedfilter'] = form.prefferedfilter.data
        settings['enablezeroconf'] = form.enablezeroconf.data
        settings['zeroconfname'] = form.zeroconfname.data
        flash(settings)
        mpd.apply(settings)

    return render_template('wizard.html', form=form)
