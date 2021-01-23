import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/record/new', methods=['POST'])
def add_record():
    # Get item from the POST body
    # only pass '{"contact_name": "Name", "contact_email_id": "mail_id", "contact_number": "phone_number"}
    req_data = request.get_json()
    record_id = helper.create_record_id()
    contact_name = req_data['contact_name']
    contact_email_id = req_data['contact_email_id']
    contact_number = req_data['contact_number']

    # Add item to the list
    res_data = helper.add_to_database(record_id, contact_name, contact_email_id, contact_number)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Record not added - '}" + record_id, status=400, mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response




if __name__ == '__main__':
    app.run()
