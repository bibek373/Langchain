from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

# Schema using Pydantic instead of TypedDict
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down the key themes mentioned in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Return the sentiment of the review either as 'pos', 'neg', or 'neutral'")
    pros: Optional[list[str]] = Field(default=None, description="List the pros mentioned in the review, if any")
    cons: Optional[list[str]] = Field(default=None, description="List the cons mentioned in the review, if any")
    name: Optional[str] = Field(default=None, description="Name of the reviewer, if mentioned")

model = ChatCohere(model="command-a-03-2025")
structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
Review by Bibek Sah""")

# Convert to dictionary
result = dict(response)
print(result['name'])

# model_dump -> pydantic official way to convert to dictionary
result_dict = response.model_dump()
print(result_dict['sentiment'])

# access attributes directly in pydantic 
print(response)
print(response.summary)
print(response.sentiment)