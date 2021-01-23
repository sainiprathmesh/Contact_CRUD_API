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


@app.route('/record/all')
def get_all_items():
    # Get items from the helper
    res_data = helper.get_all_records()
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/record/status/by_name', methods=['GET'])
def get_item_by_name():
    # Get parameter from the URL
    contact_name = request.args.get('contact_name')

    # Get items from the helper
    status = helper.get_record_by_name(contact_name)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'Item Not Found - '}" + contact_name, status=404, mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response


@app.route('/record/status/by_mail', methods=['GET'])
def get_item_by_mail():
    # Get parameter from the URL
    contact_email_id = request.args.get('contact_email_id')

    # Get items from the helper
    status = helper.get_record_by_mail(contact_email_id)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'Item Not Found - '}" + contact_email_id, status=404, mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response


@app.route('/record/remove', methods=['DELETE'])
def delete_record():
    # Get item from the POST body
    req_data = request.get_json()
    record_id = req_data['record_id']

    # Delete item from the list
    res_data = helper.delete_record(record_id)
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + record_id + "}", status=400, mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response



if __name__ == '__main__':
    app.run()
