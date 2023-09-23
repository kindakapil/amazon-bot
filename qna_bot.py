def qna(user_question):
    from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer, pipeline

    model_name = "deepset/electra-base-squad2"

    model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open('bot_input') as f:
        context = str(f.readlines())

    # Getting predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    QA_input = {
        'question': user_question,
        'context': context
    }

    res = nlp(QA_input)
    print(f"Question: {user_question}")
    print(f"Answer: {res['answer']}")
    answer = str(f"Answer: {res['answer']}")
    return answer