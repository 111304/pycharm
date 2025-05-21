# routes.py
from flask import render_template, request, redirect, url_for
from models import db, UploadedData
from forms import UploadForm
import pandas as pd
import os,csv

def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        form = UploadForm()
        if form.validate_on_submit():
            file = request.files['file']
            if file:
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)


                df = pd.read_csv(
                    file_path,
                    sep=None,  # 自动检测分隔符
                    engine='python',  # 使用Python解析引擎
                    quoting= csv.QUOTE_MINIMAL,
                    error_bad_lines=False
                )

                
                # 保存到数据库
                for _, row in df.iterrows():
                    data = UploadedData(
                        column1=row[0],
                        column2=row[1]
                    )
                    db.session.add(data)
                db.session.commit()
                print(f"成功插入 {len(df)} 条数据到数据库")
                
                return redirect(url_for('show_data'))
        return render_template('upload.html', form=form)

    @app.route('/data')
    def show_data():
        data = UploadedData.query.all()
        return render_template('display.html', data=data)

