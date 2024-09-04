import pandas as pd

from flask_wtf import FlaskForm

from wtforms import SelectField, SubmitField, IntegerField, FloatField

from wtforms.validators import DataRequired

data = pd.read_csv("X_train.csv")

class InputForm(FlaskForm):
    company = SelectField(
        label="Company",
        choices= data["Company"].unique().tolist(),
        validators=[DataRequired()]
    )
    typename = SelectField(
        label="TypeName",
        choices=data["TypeName"].unique().tolist(),
        validators=[DataRequired()]
    )
    inches = FloatField(
        label="Inches",
        validators=[DataRequired()]
    )
    screen_resolution = SelectField(
        label="ScreenResolution",
        choices=data["ScreenResolution"].unique().tolist(),
        validators=[DataRequired()]
    )
    ram = IntegerField(
        label="Ram",
        validators=[DataRequired()]
    )
    op_sys = SelectField(
        label="OpSys",
        choices=data["OpSys"].unique().tolist(),
        validators=[DataRequired()]
    )
    weight = FloatField(
        label="Weight",
        validators=[DataRequired()]
    )
    ips = IntegerField(
        label="IPS",
        validators=[DataRequired()]
    )
    touchscreen = IntegerField(
        label="Touchscreen",
        validators=[DataRequired()]
    )
    cpu_Brand = SelectField(
        label="CPU_Brand",
        choices=data["CPU_Brand"].unique().tolist(),
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
        choices=data["GPU_brand"].unique().tolist(),
        validators=[DataRequired()]
    )
    os = SelectField(
        label="OS",
        choices=data["OS"].unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
    

    
    

