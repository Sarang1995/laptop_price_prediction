import pandas as pd
import joblib

from flask import Flask, render_template, flash, url_for

from form import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "laptop_price_prediction"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET","POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            Company=[form.company.data],
            TypeName=[form.typename.data],
            Inches=[form.inches.data],
            ScreenResolution=[form.screen_resolution.data],
            Ram=[form.ram.data],
            OpSys=[form.op_sys.data],
            Weight=[form.weight.data],
            IPS=[form.ips.data],
            Touchscreen=[form.touchscreen.data],
            CPU_Brand=[form.cpu_Brand.data],
            SSD=[form.ssd.data],
            HDD=[form.hdd.data],
            Flash_Storage=[form.flash_storage.data],
            Hybrid=[form.hybrid.data],
            GPU_brand=[form.gpu_brand.data],
            OS=[form.os.data],
        ))
        prediction = model.predict(x_new)[0]
        message = f"The predicted price is {prediction} INR"
    else:
        message = f"Please enter valid inputs!!"

    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
