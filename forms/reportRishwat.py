from wtforms import Form, TextField, validators, DateField, SelectField, TextAreaField


class RegistrationForm(Form):
    date = DateField('Date it took place',format='MM-DD-YYYY',validators=[validators.required()])
    province = SelectField('Administrative Unit',
                           choices=[(1, 'Punjab'), (2, 'Sindh'), (3, 'Balochistan'), (4, 'Khyber Pakhtunkhwa')
                               , (5, 'Islamabad Capital Territory'), (6, 'Federally Administered Tribal Areas'),
                                    (7, 'Azad Jammu & Kashmir'),
                                    (8, 'Gilgit Baltistan')],coerce=int)
    location = TextField('location')
    officer = TextField('officer Name')
    bribe = TextField('bribe', [validators.required(), validators.NumberRange])
    description = TextAreaField(u'Description', [validators.optional(), validators.length(max=250)])
