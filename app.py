from flask import Flask, render_template, request
import sys
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/eda', methods=['POST'])  # This will be called from UI
def  auto_eda():
    if (request.method=='POST'):
        filename=request.form['file']
        import pandas as pd
        from pandas_profiling import ProfileReport
        df = pd.read_csv(filename)
        design_report = ProfileReport(df)
        design_report.to_file(output_file='templates/report.html')
        return render_template('report.html')





if __name__ == '__main__':
    app.run(debug=True)

