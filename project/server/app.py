import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import pickle

# pip install mysql-connector-python-rf
# pip install flask_cors
# pip install scikit-learn
# pip install pandas

# Mysql config
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# For Flask 2.3 and later use this:
app.json.sort_keys = False
CORS(app)

def get_cols():
    return 'id,name,class,academic_performance,technical_skills,core_knowledge,puzzle_solving,programming_skills,group_discussion_score,project,internship,backlog,coding_skills,aptitude_skills,communication_skills,presentation_skills,english_proficiency,management_skills,training,result'

# 404 page
@app.errorhandler (404)
def not_found (error=None):
    response = {
        'message': 'Invalid request',
    }
    return jsonify(response)

@app.route('/predict', methods = ['POST'])
def predict():
    form = request.form.values()
    data = [x for x in form]

    if(len(data) < 18):
        response = {
            'response' : '16 inputes expected '+len(data)+' received.'
        }
        return jsonify(response), 200
    
    predict_data = [int(e) for e in data if e not in (data[0],data[1])]
    
    # Load model
    model = pickle.load(open('predictor.pickle', 'rb'))
    
    rawRes = model.predict([predict_data])
    
    res = rawRes[0]*100

    predict_data.append(float(res))
    predict_data.insert(0,data[0])
    predict_data.insert(1,data[1])
    
    colsStr = get_cols()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="plecematepro"
    )

    # Create cursor object
    cursor = conn.cursor()
    
    sql = "INSERT INTO data (name, class, academic_performance, technical_skills, core_knowledge, puzzle_solving, programming_skills, group_discussion_score, project,internship, backlog, coding_skills, aptitude_skills, communication_skills, presentation_skills, english_proficiency, management_skills, training, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    strParms = '"'+data[0]+'","'+data[1]+'",'
    strParms += ','.join([str(elem) for elem in predict_data])

    cursor.execute(sql, predict_data)

    conn.commit()

    response = {
        "result" : res
    }
    
    # Return response
    return jsonify(response), 200

    
@app.route('/result', methods=['GET'])
def get_result():

    # Error handling
    try:
        # Accept request
        filters = request.args.get('filter')

        # Request empty?        
        if(filters != None):
            colsStr = filters;

        # Create connection object
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plecematepro"
        )

        # Create cursor object
        cursor = conn.cursor()

        # Get column names
        colsStr = get_cols()


        # Execute select command to fetch data
        cursor.execute('SELECT '+colsStr+' FROM data')

        # Fetch all records
        result = cursor.fetchall()

        # Convert string into array
        cols = colsStr.split(',')

        # Create empty dictionary for storing values
        data = {};

        # convert data in key and pair format
        i = 0
        for row in result:
            tmpdata = {}
                
            for j in range(0, len(row)):
                # Store records in key and pair format in dictionary
                tmpdata[cols[j]] = row[j]

            # Store Key pair values into list
            data[i] = tmpdata
            i+=1

        # Create response 
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

        # Return response
        return jsonify(response), 200
    
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()

        
if __name__ == '__main__':
    # Start development server
    app.run(host='127.0.0.1', port=8081)

