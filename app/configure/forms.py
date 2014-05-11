# -*- encoding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField, \
    PasswordField, validators
from wtforms.validators import Length
from ..mpd import availableinterfaces
from os import getenv

logname = getenv('LOGNAME')


class WizardForm(Form):
    aiflist = availableinterfaces()
    overwriteconf = BooleanField(u'Overwrite existing configuration file?',
                                 default=True)
    interface = SelectField(u'Interfaces',
                            default='',
                            choices=aiflist,
                            description='Select the audio interface')
    interfacetype = StringField(u'Path', default='usb',
                                description='Filter by type')
    enablezeroconf = BooleanField(u'Enable')
    zeroconfname = StringField(u'Name of service',
                               description='Leave empty for default',
                               default='',
                               validators=[Length(0, 64)])
    musicdir = StringField(u'Music directory',
                           default='/home/{0}/Music'.format(logname))
    password = PasswordField('Password for {0}'.format(logname),
                             [validators.Required()])
    submit = SubmitField('Submit')
