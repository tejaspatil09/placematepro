import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

# pip install mysql-connector-python-rf
# pip install flask_cors

# Mysql config
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# For Flask 2.3 and later use this:
app.json.sort_keys = False
CORS(app)

# 404 page
@app.errorhandler (404)
def not_found (error=None):
    response = {
        'message': 'Invalid request',
    }
    return jsonify(response)

@app.route('/post', methods=['GET'])
@app.route('/result', methods=['GET'])

def get_result():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plecematepro"
        )
        
        filters = request.args.get('filter')

        colsStr = 'name,class,academic_performance,technical_skills,core_knowledge,puzzle_solving,programming_skills,project,internship,backlog,coding_skills,aptitude_skills,communication_skills,presentation_skills,english_proficiency,management_skills,result';
        if(filters != None):
            colsStr = filters;
        
        cur = conn.cursor()
        cur.execute('SELECT '+colsStr+' FROM data')
        result = cur.fetchall()
        alldata = [];

        cols = colsStr.split(',')
        
        data = {};

        try:
            i = 0
            for row in result:
                tmpdata = {}

                for j in range(0, len(row)):
                    tmpdata[cols[j]] = row[j];

                data[i] = tmpdata
                
                i+=1
        except Exception as e:
            print(e)

        response = {
            'app' : 'plecematepro',
            'request': request.remote_addr,
            'api_version' : 1.0,
            'status' : 200,
            'data' : {
                'cols' : cols,
                'record' : data
            }
        }
        
        return jsonify(response), 200
    except Exception as e:
        print(e)
    finally:
        cur.close()

        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)

