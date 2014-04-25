from flask import render_template, flash, redirect, url_for
from . import configure
from .forms import WizardForm
from ..mpd import applysettings


@configure.route('/')
def index():
    return render_template('configure/index.html')


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardForm()
    if form.validate_on_submit():
        settings = {'DRYRUN': 'True'}
        import ipdb; ipdb.set_trace()
        settings['MPD_CONFFILE'] = form.mpdconfpath.data
        settings['MPD_MUSICDIR'] = form.musicdir.data
        settings['LIMIT_INTERFACE_FILTER'] = form.interface.data
        flash(settings)
        applysettings(settings)
        return redirect(url_for('configure.index'))

    return render_template('configure/wizard.html', form=form)
