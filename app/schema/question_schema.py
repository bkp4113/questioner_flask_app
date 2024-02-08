from cerberus import Validator


question_schema = {
    'questionText': {'type': 'string', 'required': True, 'min': 10, 'max': 50},
    'choices': {
        'type': 'list',
        'minlength': 2,
        'maxlength': 5,
        'schema': {
            'type': 'dict',
            'schema': {
                'key': {'type': 'string'},
            },
            'allow_unknown': True
        }
    }
}


def validate(data: dict, schema:dict=question_schema) -> tuple[bool, str]:

    v = Validator()

    if v.validate(data, schema):
        return True, None
    else:
        return False, v.errors

