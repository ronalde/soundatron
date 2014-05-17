from flask import render_template, redirect, url_for
from . import configure
from .forms import WizardForm
from .mpd import applympdconf, availableinterfaces


@configure.route('/')
def index():
    return render_template('configure/index.html')


@configure.route('/wizard/', methods=['GET', 'POST'])
def wizard_apply():
    form = WizardForm()
    form.interface.choices = [(i[0], i[1]) for i in availableinterfaces()]
    if form.validate_on_submit():
        settings = {}
        settings['LIMIT_INTERFACE_FILTER'] = '"{0}"'.format(form.interface.data)
        settings['G_PATHS_MUSICDIRECTORY'] = '"{0}"'.format(form.musicdir.data)
        settings['G_ZEROCONF_ZEROCONFNAME'] = '"{0}"'.format(form.zeroconfname.data)
        password = form.password.data
        applympdconf(settings, password)
        return redirect(url_for('configure.index'))

    return render_template('configure/wizard.html', form=form)
