# -*- encoding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import Length


class WizardForm(Form):

    musicdir = StringField('Music Directory', default='/var/lib/mpd/music', )
    prefferedfilter = StringField('Type filter', default='USB Audio')
    enablezeroconf = BooleanField('enable Zero Conf')
    zeroconfname = StringField('Zero Conf Name', default='soundatron',
                               validators=[Length(0, 64)])
    submit = SubmitField('Submit')
