from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())
model = ChatCohere(model = 'command-a-03-2025')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a joke on a following {topic}',
    input_variables=['topic']
)

joke_gen_chain =  RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'],result['word_count'])

print(final_result)