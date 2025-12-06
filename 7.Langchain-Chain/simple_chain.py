from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template = PromptTemplate(
    template = 'Generate intresting 5 facts about {topic}',
    input_variables=['topic']    
)

model = ChatCohere(model = "command-a-03-2025")

parser = StrOutputParser()

chain = template | model | parser


result = chain.invoke({'topic':'Nepal'})


print(result)

chain.get_graph().print_ascii()