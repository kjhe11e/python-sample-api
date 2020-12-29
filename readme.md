## A simple Python3 API server

### Background

This API server provides a single API: GET /employees.

For context please read: https://gist.github.com/kpurdon/ac43d733370e89824304e89d3ec502bf


### Setup instructions

#### Running locally

```
1. git clone https://github.com/kjhe11e/python-sample-api-server.git
2. cd python-sample-api-server
3. python3 -m venv venv
4. source venv/bin/activate
5. python3 -m pip install -r requirements.txt
* Note: the next step assumes you are using Bash shell, if not please refer to your shell's documentation for setting environment variables.
6. export PORT={your_port_number} && python app.py

  - where {your_port_number} is your desired port number (without the curly braces); e.g. 8200

Example:
    export PORT=8200 && python app.py
```

### Verifying the API

Assuming you opened another terminal window/session for testing the API, you may need to redefine your PORT environment variable since environment variables are often "local" to that particular shell session (like when using `Bash` for example). If needed, run `export $PORT={your_port_number}` in your new shell session using the same port value specified when you ran the setup instructions above. For example, following the setup example command in step 6a above, run `export PORT=8200`.

Verify your PORT environment variable is set, e.g. if Bash shell run `echo $PORT`

Then test the API endpoint:

`curl localhost:$PORT/employees`

You should get a response like:

```
[
  {
    "id": 1,
    "gender": "male"
  },
  {
    "id": 2,
    "gender": "male"
  },
  {
    "id": 3,
    "gender": "male"
  },
  {
    "id": 4,
    "gender": "female"
  },
  {
    "id": 5,
    "gender": "female"
  },
  {
    "id": 6,
    "gender": "female"
  }
]
```

