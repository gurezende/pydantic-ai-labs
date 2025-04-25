# Imports
import os
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.exceptions import ModelHTTPError

# Instantiate the models
openai_model = OpenAIModel('gpt-4o')
google_model = GeminiModel('gemini-1.5-flash')

# Create the Fallback model
fallback_model = FallbackModel(openai_model, google_model)

# Run the agent
agent = Agent(fallback_model,
              retries=2,
              api_base=os.environ.get("OPENAI_API_KEY"),
            #   api_key=os.environ.get("GEMINI_API_KEY"),
              system_prompt='Be concise, use a single sentence.')

# Response
try:
    response = agent.run_sync('What is the most populated city in the world?')
    print(response.output)

except ModelHTTPError as errors:
    for error in errors:
        print(error)

print(response.all_messages())