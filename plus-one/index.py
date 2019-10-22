# Copyright (c) Alex Ellis 2017. All rights reserved.
# Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
import json
import shutil
import config
from json import JSONDecodeError
from urllib.error import URLError

from function import handler
from function import preprocess_params

def get_params_from_stdin() -> dict:
    buf = ""
    while True:
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    return json.loads(buf)



def handle_error(error, message='Unknown error, please ask the admins to check container logs for more info'):
    # This will be written to container logs
    sys.stderr.write(f'Error from function: {str(error)}\n\n')

    # This will be sent back to caller/server
    start = "Error from function: "

    if type(error) is not ValueError:
        result = start + str(message)
    else:
        result = start + str(error)
    print(json.dumps({"function_status": "error",
                      "result": result}))

def handle_success(result):
    print(json.dumps({"function_status": "success",
                      "result": result}))

if __name__ == "__main__":
    try:
        # Get and parse params
        params = get_params_from_stdin()

        # Mutate the params to get them ready for use
        preprocess_params.preprocess(params)

        # Run!
        function_response = handler.handle(params)
        handle_success(function_response)

    except JSONDecodeError as e:
        handle_error(e, "Request received by function is not valid JSON. Please check docs")

    except URLError as e:
        handle_error(e, "Problem downloading files. Please check URLs passed as parameters are "
                        "valid, are live and are publicly accessible.")
