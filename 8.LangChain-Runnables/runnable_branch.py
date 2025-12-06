from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv

load_dotenv()


model = ChatCohere(model = 'command-a-03-2025')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate the report on the following {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following {report}',
    input_variables=['report']
)


report_gen_chain = RunnableSequence(prompt1, model, parser)


branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic':'India vs Pakistan'})

print(result)
