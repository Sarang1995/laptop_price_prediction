import pandas as pd

from flask_wtf import FlaskForm

from wtforms import SelectField, SubmitField, IntegerField, FloatField

from wtforms.validators import DataRequired

data = pd.read_csv("X_train.csv")

class InputForm(FlaskForm):
    company = SelectField(
        label="Company",
        choices= data["company"].unique().tolist(),
        validators=[DataRequired()]
    )
    typename = SelectField(
        label="TypeName",
        choices=data["typename"].unique().tolist(),
        validators=[DataRequired()]
    )
    inches = FloatField(
        label="Inches",
        validators=[DataRequired()]
    )
    screen_resolution = SelectField(
        label="ScreenResolution",
        choices=data["screenresolution"].unique().tolist(),
        validators=[DataRequired()]
    )
    ram = IntegerField(
        label="Ram",
        validators=[DataRequired()]
    )
    opsys = SelectField(
        label="OpSys",
        choices=data["opsys"].unique().tolist(),
        validators=[DataRequired()]
    )
    weight = FloatField(
        label="Weight",
        validators=[DataRequired()]
    )
    ips = SelectField(
        label="IPS",
        choices=data["ips"].unique().tolist(),
        validators=[DataRequired()]
    )
    touchscreen = SelectField(
        label="Touchscreen",
        choices=data["touchscreen"].unique().tolist(),
        validators=[DataRequired()]
    )
    cpu_Brand = SelectField(
        label="CPU_Brand",
        choices=data["cpu_brand"].unique().tolist(),
        validators=[DataRequired()]
    )
    ssd = IntegerField(
        label="SSD",
        validators=[DataRequired()]
    )
    hdd = IntegerField(
        label="HDD",
        validators=[DataRequired()]
    )
    flash_storage = IntegerField(
        label="Flash Storage",
        validators=[DataRequired()]
    )
    hybrid = IntegerField(
        label="Hybrid",
        validators=[DataRequired()]
    )
    gpu_brand = SelectField(
        label="GPU_brand",
        choices=data["gpu_brand"].unique().tolist(),
        validators=[DataRequired()]
    )
    os = SelectField(
        label="OS",
        choices=data["os"].unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
    

    
    

