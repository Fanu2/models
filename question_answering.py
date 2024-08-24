from transformers import pipeline

def answer_question(question, context):
    qa = pipeline('question-answering')
    result = qa(question=question, context=context)
    return result['answer']

# Example usage
context = 'Hugging Face is a company specializing in Natural Language Processing.'
print(answer_question('What does Hugging Face specialize in?', context))
