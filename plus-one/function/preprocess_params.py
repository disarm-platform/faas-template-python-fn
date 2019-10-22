def preprocess(params: dict):
    if 'number' in params:
        if type(params['number']) is not int:
            raise ValueError('number needs to be a number')
    else:
        raise ValueError('Input should have number')

    # params['stats'] if exists must match the possible optio
