from flask_wtf import FlaskForm 
from flask_wtf.file import FileFeild, FileRequired, FileAllowed 
from wtform import TextAreaFeild, FileFeild
from wtforms.validators import DataRequired  

class UploadForm(FlaskForm):
    Description=TextAreaFeild('Description',validators=[DataRequired()])
    Photo=FileFeild('Photo',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
