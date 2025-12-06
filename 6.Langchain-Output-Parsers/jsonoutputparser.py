from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name , age and city of a fictional person \n {format_instructions}',
    input_variables= [],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template.format()

# response = model.invoke(prompt)
# parser_response = parser.parse(response.content)

# easier way using chain
chain = template | model | parser
parser_response = chain.invoke({})


print(parser_response)
print(type(parser_response))