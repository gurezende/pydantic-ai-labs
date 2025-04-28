# Imports
import os
import random
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field
from typing import List, Dict
import pandas as pd

# Creating an agent
agent = Agent(
    model='google-gla:gemini-1.5-flash', 
    api_key=os.environ.get("GEMINI_API_KEY"),
    system_prompt='Generate lottery numbers.'
              )


# Tool that cannot access the context
@agent.tool_plain  
def generate_lottery_number() -> str:
    """Generate a lottery game with 6 numbers."""
    numbers = list(random.sample(range(1, 69), 5))
    numbers.append(random.randint(1, 25))
    return numbers


result = agent.run_sync('Generate a lottery game.')

print(result.output)

# Notice in the messages that the agent uses the tool
print(result.all_messages())

### OUTPUT ###

#Your lottery numbers are: 16, 68, 67, 41, 63, 11.  Good luck!
# ModelRequest(parts=[ToolReturnPart(tool_name='generate_lottery_number', content=[16, 68, 67, 41, 63, 11], 
