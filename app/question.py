from flask_restx import Resource
from flask import request
from app.swagger.question_swagger import question_ns, question_model
from flask import abort, jsonify
from app.schema.question_schema import validate


@question_ns.route("/")
class Question(Resource):

    @question_ns.expect(question_model)
    @question_ns.response(200, "Question created.", question_model)
    @question_ns.response(400, "Question validation failed.")
    def post(self):

        data = request.get_json()
        status, error = validate(data)

        if not status:
            abort(400, f"Question validation failed for {error}")

        new_question = Question(
            questionText=data.get('questionText'),
            choices=data.get('choices')
        )

        db.session.add(new_question)
        db.session.commit()

        return jsonify({
            'id': new_question.id,
            'questionText': new_question.questionText,
            'choices': new_question.choices
        }), 200

    @question_ns.response(200, "Question returned", [question_model])
    def get(self):

        questions = Question.query.all()
        questions_data = []
        for question in questions:
            questions_data.append({
                'id': question.id,
                'questionText': question.questionText,
                'choices': question.choices
            })
        return jsonify(questions_data), 200


@question_ns.route("/<int:question_id>")
class QuestionObject(Resource):

    @question_ns.response(200, "Question resource returned.", question_model)
    @question_ns.response(404, "Question resource not found.")
    def get(self, question_id):

        question = Question.query.get(question_id)
        if question:
            return jsonify({
                'id': question.id,
                'questionText': question.questionText,
                'choices': question.choices
            })
        else:
            return jsonify({'message': 'Question resource not found'}), 404

    @question_ns.expect(question_model)
    @question_ns.response(200, "Question updated.")
    @question_ns.response(400, "Question validation failed.")
    @question_ns.response(404, "Question resource not found.")
    def put(self, question_id):

        data = request.get_json()
        question = Question.query.get(question_id)
        if not question:
            return jsonify({'message': 'Question resource not found'}), 404

        questionText = data.get('questionText')
        choices = data.get('choices')

        if questionText:
            question.questionText = questionText
        if choices:
            question.choices = choices

        db.session.commit()

        return jsonify({'message': 'Question updated successfully'}), 200

    @question_ns.response(200, "Question deleted.")
    @question_ns.response(404, "Question resource not found.")
    def delete(self, question_id):

        question = Question.query.get(question_id)
        if not question:
            return jsonify({'message': 'Question resource not found.'}), 404

        db.session.delete(question)
        db.session.commit()

        return jsonify({'message': 'Question deleted.'}), 200

