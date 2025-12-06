from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Use TinyLlama - it has chat template support
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Nepal?")
print(result.content)