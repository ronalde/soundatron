# -*- encoding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField, \
    PasswordField
from wtforms.validators import Length
from ..mpd import availableinterfaces


class WizardForm(Form):
    aiflist = availableinterfaces()
    mpdconfpath = StringField(u'Path', default='~/mpd.conf', )
    overwriteconf = BooleanField(u'Overwrite existing configuration file?',
                                 default=True)
    interface = SelectField(u'Interfaces',
                            default='',
                            choices=aiflist,
                            description='Select the audio interface to use for mpd')
    enablezeroconf = BooleanField(u'Enable')
    zeroconfname = StringField(u'Name of service',
                               description='Leave empty for default',
                               default='',
                               validators=[Length(0, 64)])
    musicdir = StringField(u'Music directory',
                           default='/var/lib/mpd/music', )
    submit = SubmitField('Submit')
