from flask import Flask, render_template, jsonify, current_app
import pymysql.cursors

app = Flask(__name__)

app.config.from_pyfile('.env')


connection = pymysql.connect(
    host=app.config['DATABASE_HOST'],
    user=app.config['DATABASE_USER'],
    password=app.config['DATABASE_PASSWORD'],
    db=app.config['DATABASE_NAME'],
    charset=app.config['DATABASE_CHARSET'],
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

@app.route('/test')
def test():
    return app.config['DATABASE_HOST']




if __name__ == "__main__":
    app.run()
