import pandas as pd
import numpy as np
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
            company=[form.company.data],
            typename=[form.typename.data],
            inches=[form.inches.data],
            screenresolution=[form.screen_resolution.data],
            ram=[form.ram.data],
            opsys=[form.opsys.data],
            weight=[form.weight.data],
            ips=[form.ips.data],
            touchscreen=[form.touchscreen.data],
            cpu_brand=[form.cpu_Brand.data],
            ssd=[form.ssd.data],
            hdd=[form.hdd.data],
            flash_storage=[form.flash_storage.data],
            hybrid=[form.hybrid.data],
            gpu_brand=[form.gpu_brand.data],
            os=[form.os.data],
        ))
        prediction = round(np.exp(model.predict(x_new)[0]),2)
        message = f"The predicted price is {prediction} INR"
    else:
        message = f"Please enter valid inputs!!"

    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
