from flask import Flask, render_template, jsonify
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def main():
    variables = {"company_name": "前进精密"}
    return render_template('index.html', company_name=variables["company_name"])

@app.route('/db')
def db():
    with connection.cursor() as cursor:
        sql = "select * from test"
        cursor.execute(sql)
        result = cursor.fetchone()
        return jsonify(result)



if __name__ == "__main__":
    app.run()
