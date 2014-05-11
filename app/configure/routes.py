from flask import render_template, flash, redirect, url_for
from . import configure
from .forms import WizardForm
from ..mpd import applympdconf


@configure.route('/')
def index():
    return render_template('configure/index.html')


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardForm()
    if form.validate_on_submit():
        settings = {}
        settings['MPD_MUSICDIR'] = form.musicdir.data
        settings['LIMIT_INTERFACE_FILTER'] = form.interface.data
        settings['LIMIT_INTERFACE_TYPE'] = form.interfacetype.data
        password = form.password.data
        flash(settings)
        applympdconf(settings, password)
        return redirect(url_for('configure.index'))

    return render_template('configure/wizard.html', form=form)
