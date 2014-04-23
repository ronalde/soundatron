# -*- encoding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,  SubmitField
from wtforms.validators import Length


class WizardForm(Form):

    musicdir = StringField('Music Directory', default='/var/lib/mpd/music', )
    zeroconfname = StringField('Zero Conf Name', default='soundatron',
                               validators=[Length(0, 64)])
    submit = SubmitField('Submit')
