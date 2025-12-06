from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate the tweet about the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate the Linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatCohere(model='command-a-03-2025')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'Linkedin':RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)