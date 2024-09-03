import pandas as pd

from flask_wtf import FlaskForm

from wtforms import SelectField, FloatField, SubmitField

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
    inches = SelectField(
        label="Inches",
        choices=data["Inches"].unique().tolist(),
        validators=[DataRequired()]
    )
    screen_resolution = SelectField(
        label="ScreenResolution",
        choices=data["ScreenResolution"].unique().tolist(),
        validators=[DataRequired()]
    )
    ram = SelectField(
        label="Ram",
        choices=data["Ram"].unique().tolist(),
        validators=[DataRequired()]
    )
    op_sys = SelectField(
        label="OpSys",
        choices=data["OpSys"].unique().tolist(),
        validators=[DataRequired()]
    )
    weight = FloatField(
        label="Weight",
        choices=data["Weight"].unique().tolist(),
        validators=[DataRequired()]
    )
    ips = SelectField(
        label="IPS",
        choices=data["IPS"].unique().tolist(),
        validators=[DataRequired()]
    )
    touchscreen = SelectField(
        label="Touchscreen",
        choices=data["Touchscreen"].unique().tolist(),
        validators=[DataRequired()]
    )
    cpu_Brand = SelectField(
        label="CPU_Brand",
        choices=data["CPU_Brand"].unique().tolist(),
        validators=[DataRequired()]
    )
    ssd = SelectField(
        label="SSD",
        choices=data["SSD"].unique().tolist(),
        validators=[DataRequired()]
    )
    hdd = SelectField(
        label="HDD",
        choices=data["HDD"].unique().tolist(),
        validators=[DataRequired()]
    )
    flash_storage = SelectField(
        label="Flash Storage",
        choices=data["Flash Storage"].unique().tolist(),
        validators=[DataRequired()]
    )
    hybrid = SelectField(
        label="Hybrid",
        choices=data["Hybrid"].unique().tolist(),
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
    

    
    

