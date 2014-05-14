# -*- encoding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, \
    PasswordField, validators, SelectField
from wtforms.validators import Length
from os import getenv


class WizardForm(Form):

    overwriteconf = BooleanField(u'Overwrite existing configuration file?',
                                 default=True),
    interface = SelectField(u'Interfaces',
                            description='Select the audio interface')
    interfacetype = StringField(u'Path', default='usb',
                                description='Filter by type')
    enablezeroconf = BooleanField(u'Enable')
    zeroconfname = StringField(u'Name of service',
                               description='Leave empty for default',
                               default='',
                               validators=[Length(0, 64)])
    musicdir = StringField(u'Music directory',
                           default='/home/{0}/Music'.format(getenv('LOGNAME'))),
    password = PasswordField('Password for {0}'.format(getenv('LOGNAME')),
                             [validators.Required()])
    submit = SubmitField('Submit')
