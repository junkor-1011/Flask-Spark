#!/usr/bin/env python
import json, io, datetime, codecs, os, random

from flask import Flask, render_template, request, jsonify, make_response,\
    send_file, session, abort, flash, url_for, redirect

from SparkDriver import SparkDriver     # TMP   本当は処理用の別コードを用意し、その応答だけを受け取る

app = Flask(__name__)

app.secret_key = "secret key"               # TMP
#app.config['SECRET_KEY'] = os.urandom(24)   # TMP


@app.before_request
def before_request():
   if request.path.startswith('/static/'):
       return
   if session.get('username') is not None:
       return
   if request.path == '/login':
       return
   return redirect('/login')


@app.errorhandler(401)
def unauthorized_error_handle(error):
    return render_template('401.html'), 401


@app.route('/', methods=['get'])
def site_root():
    return redirect("/menu")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and _is_account_valid():
        uid = request.form['uid']
        username, setting = _get_user_info(uid)
        session['uid'] = uid
        session['username'] = username
        session['setting'] = setting
        session['spark'] = None         # TMP

        return redirect(url_for('menu'))    # auth success
    elif request.method == 'POST' and (not _is_account_valid()):
        abort(status=401)

    else:
        title = "login"
        return render_template('login.html', title=title)


@app.route('/logout')
def logout():
    session.pop('uid', None)
    session.pop('username', None)
    session.pop('setting', None)
    session.pop('spark', None)
    return redirect(url_for('login'))


@app.route('/menu', methods=['GET'])
def menu():
    title = "Main Menu"
    return render_template('menu.html', title=title)


@app.route('/leaflet_test1', methods=['GET'])
def leaflet_test1():
    title = "Leaflet Test1"
    return render_template('leaflet_test1.html', title=title)


@app.route('/table_test1', methods=['GET'])
def table_test1():
    title = "Table Test1"
    return render_template('table_test1.html', title=title)


@app.route('/graph_test1', methods=['GET'])
def graph_test1():
    title = "Graph Test1"
    return render_template('graph_test1.html', title=title)


@app.route('/post_utils/read_spark_table_tmp', methods=['POST'])
def read_spark_table_tmp():
    sd = SparkDriver()
    spark = sd.spark
    table = request.form['table']
    limit = request.form['limit']
    df = spark.sql(f"""
        SELECT * FROM {table} LIMIT {limit}
""")
    #df.cache()
    #df.show(limit)  # TMP  # py4j.protocol.Py4JError: An error occurred while calling o86.showString. が出る（他にも意図しない挙動が起きていないかチェックする必要）
    pdf = df.toPandas()
    return pdf.to_html()



def _is_account_valid():    # TMP
    uid = request.form.get('uid')
    pwd = request.form.get('pwd')
    if uid == 'admin' and pwd == 'pwd':
        # auth-success
        return True

    # auth-failed
    return False


def _get_user_info(uid):
    """
    uidをキーにしてDataBaseから諸々の必要情報を引っ張ってくるイメージ

    :arg
    """
    # TMP   暫定処置
    name = uid      # ToDo: DBから持ってくるようにする
    setting = {}    # ToDO: DBから持ってくるようにする
    return name, setting


if __name__ == '__main__':
    app.debug = True
    app.run(
            host='0.0.0.0',
            port=5001,
            ssl_context=('ssl/server.crt', 'ssl/server.key'),
            threaded=True
            )

