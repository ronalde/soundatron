from flask import render_template, flash, redirect, url_for
from . import configure
from .forms import WizardForm
from ..mpdconfigure import MpdConfigure

mc = MpdConfigure()


@configure.route('/')
def index():
    return render_template('configure/index.html')


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardForm()
    if form.validate_on_submit():
        settings = {'DEBUG': 'True', 'DRYRUN': 'True'}
        settings['prefferedfilter'] = form.prefferedfilter.data
        settings['enablezeroconf'] = form.enablezeroconf.data
        settings['zeroconfname'] = form.zeroconfname.data
        flash(settings)
        mc.apply(settings)
        return redirect(url_for('configure.index'))
        flash("cool")

    return render_template('configure/wizard.html', form=form)
