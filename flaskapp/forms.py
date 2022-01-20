from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskapp.models import User


class Register(FlaskForm):
    name = StringField(label='Full Name', validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    city = StringField(label='City', validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField('Save')

    # Validar que el email sea único
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already in use')
