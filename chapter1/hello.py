from pydantic_ai import Agent
from pydantic_ai.common_tools.duckduckgo import duckduckgo_search_tool
from pydantic import BaseModel
import os

# agent = Agent(  
#     'google-gla:gemini-1.5-flash',
#     api_key=os.environ.get("GEMINI_API_KEY"),
#     system_prompt='Be concise, reply with less than 100 words a post for LinkedIn in Markdown notation and containing a small code snippet. The code does not count towards the word count.',  
# )

# Output Type
class Answer(BaseModel):
    city: str
    year: int

output_type = Answer

agent = Agent(
    'google-gla:gemini-1.5-flash',
    api_key=os.environ.get("GEMINI_API_KEY"),
    tools=[duckduckgo_search_tool()],
    model_settings={'temperature': 0.5},
    system_prompt='Be concise, reply with one sentence.',
    output_type=output_type,
    verbose=True
)

result = agent.run_sync(user_prompt='what is the city of the last Summer Olympic Games in the USA and the year')  
print(result.output)
