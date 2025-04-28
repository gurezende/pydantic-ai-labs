from dataclasses import dataclass
import httpx
import os
from pydantic_ai import Agent, RunContext


@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'google-gla:gemini-1.5-flash',
    api_key=os.environ.get("GEMINI_API_KEY"),
    deps_type=MyDeps,
)

'''Explanation of injection by RunContext:
Once the MyDeps instance is created and its attributes are populated, 
the framework makes this instance accessible within the RunContext object 
that is passed as an argument to the agent's methods (like get_system_prompt). 
This is why we can access the api_key and http_client using ctx.deps (injection). 
The deps attribute of the RunContext acts as a container for the injected dependencies.'''

@agent.system_prompt  
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
    # MyDeps injected into RunContext becomes ctx.deps.[variable]
    response = await ctx.deps.http_client.get(  
        'https://example.com',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},  
    )
    print(response)
    response.raise_for_status()
    return f'Prompt: {response.text}'

async def main():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run('Tell me a joke about Python.', deps=deps)
        print(result.output)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())