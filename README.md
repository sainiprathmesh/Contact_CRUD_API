# Contact_CRUD_API


<h1>For creating the table :</h1>
<code>create table records
(
    record_id        integer
        primary key autoincrement,
    contact_name     varchar(30) not null,
    contact_email_id varchar(50)
        unique,
    contact_number   bigint(11)  not null
);</code>

<h3>1. I use SQLite for database connectivity.</h3>
<h3>2. I make contact_email_id as unique key for reducing the complexity.</h3>
<h3>3. We can use redis for O(1) complexity in insertion and searching. (Paid Service)</h3>

<h1>For testing the code :</h1>

<h3>1. I use curl commands.</h3>

<h2>For starting API :</h2> <code>$ FLASK_APP=app.py flask run</code>

<h2>For Adding Contact :</h2>
<h3> Contact should be in JSON format.</h3>

<code>$ curl -X POST http://127.0.0.1:5000/record/new -d '{"contact_name": "name", "contact_email_id": "mailid", "contact_number": "0000000000"}' -H 'Content-Type: application/json'</code>

<h2>For Viewing Contact :</h2>
<h3>You'll have to pass the page number for viewing the data of that page because pagination of 10 data per page is also implemented.</h3>
<code>$ curl -X GET http://127.0.0.1:5000/record/all?page_no=1 </code>

<h2>For Searching Contact by Name:</h2>
<h3>You'll have to pass the name with query string.</h3>
<code>$ curl -X GET http://127.0.0.1:5000/record/status/by_name?contact_name=pra </code>

<h2>For Searching Contact by Mail ID:</h2>
<h3>You'll have to pass the mail id with query string.</h3>
<code>$ curl -X GET http://127.0.0.1:5000/record/status/by_mail?contact_email_id=prathmesh@gla.ac.in
</code>

<h2>For Updating Record by record_id:</h2>
<code>$ curl -X PUT http://127.0.0.1:5000/record/update -d '{"record_id": 10, "new_contact_name": "Prathmesh Kumar Saini", "new_contact_mail": "prathmesh.saini_cs18@gla.ac.in", "new_contact_number": "7080762239"}' -H 'Content-Type: application/json'</code>

<h2>For Deleting Record by record_id:</h2>
<code>$ curl -X DELETE http://127.0.0.1:5000/record/remove -d '{"record_id": 9}' -H 'Content-Type: application/json'</code>

<h1>Note : All validation of data will be done on client side.</h1>

