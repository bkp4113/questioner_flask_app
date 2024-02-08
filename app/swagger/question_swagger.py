from flask_restx import Namespace, fields

question_ns = Namespace('question', 'Question endpoint')

choice_model = question_ns.model('Choice Model', {
    'option_1': fields.String('Choice Options K,V pairs')
})

question_model = question_ns.model('Question Model', {
    'questionText': fields.String(description='Question text', required=True, min_length=10, max_length=50),
    'choices': fields.List(fields.Nested(choice_model, allow_null=False), min=2, max=5)
})
