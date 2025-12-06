from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate the detailed report on the  {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate the 5 pointer summary of the text\n {text}',
    input_variables=['text']
)

model = ChatCohere(model='command-a-03-2025')

parser = StrOutputParser()

chain = prompt1 | model | parser |prompt2 | model | parser

result = chain.invoke({'topic':'Nepal'})

print(result)

chain.get_graph().print_ascii()