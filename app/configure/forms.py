# -*- encoding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField,\
    validators, SelectField
from wtforms.validators import Length
from os import getenv


class WizardForm(Form):
    logname = getenv('LOGNAME')
    overwriteconf = BooleanField(u'Overwrite existing configuration file?',
                                 default=True),
    interface = SelectField(u'Interfaces',
                            description='Select the audio interface')
    zeroconfname = StringField(u'Name of ZeroConf service',
                               description='Leave empty for default',
                               default='soundatron',
                               validators=[Length(0, 64)])
    musicdir = StringField(u'Music directory',
                           default='/home/{0}/Music'.format(logname))
    password = PasswordField('Password for {0}'.format(logname),
                             [validators.Required()])
    submit = SubmitField('Submit')
