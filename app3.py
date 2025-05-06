
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# PostgreSQL RDS credentials
DB_HOST = 'dsherzod3t.c32geugqgvkj.ap-southeast-1.rds.amazonaws.com'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'djambull11'

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/fetch_student', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sherzod.sherzod;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO sherzod.sherzod (
            gender, race_ethnicity, parental_level_of_education,
            lunch, test_preparation_course, math_score,
            reading_score, writing_score
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        data['gender'], data['race_ethnicity'], data['parental_level_of_education'],
        data['lunch'], data['test_preparation_course'],
        int(data['math_score']), int(data['reading_score']), int(data['writing_score'])
    ))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/delete_student', methods=['POST'])
def delete_student():
    data = request.json
    math_score = int(data['math_score'])
    reading_score = int(data['reading_score'])
    writing_score = int(data['writing_score'])

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM sherzod.sherzod
        WHERE math_score = %s AND reading_score = %s AND writing_score = %s
    ''', (math_score, reading_score, writing_score))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
