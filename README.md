Messages API

Getting started
Install Flask - pip install Flask.
Install pytest - pip install pytest.
use postman or equivalent.

to use the API get, post and delete methods, use postman. 
copy the link you receive when running the python app.py command in terminal and add the method route. besides, at the left of the link choose the right method you are currently using.
post - /AddMessage and in the 'body' of postman put the message you want to add in a json format. for example:
{
        "application_id": 3,
        "session_id": "kkk",
        "message_id": "lll",
        "participants": ["Israel Israeli", "Albert Einstein"],
        "content": "Nice to meet you, Albert"
}

get -/GetMessgae?[get message by]=[id]
right after the question mark, mention what property would you like to receive the messages by (application_id, session_id, or message_id), equals to the property id.
for example: /GetMessage?session_id=bbb

delete -/DeleteMessage?[get message by]=[id] right after the question mark, mention what property would you like to delete the messages by (application_id, session_id or message_id), equals to the property id.
for example: /DeleteMessage?application_id=1

Running the tests
Go to terminal and run the command - python app.py, that would run the app on the localhost.
while the application is running, open another terminal and run the command - pytest.

When running pytest, multiple tests would run to check if the API methods works as expected, writing, selecting and deletining from the sqlite database works. 

Built With
flask microframwork
sqlite database

I used the commented section in the app.py bellow the header #create_database to create the sqlite db.