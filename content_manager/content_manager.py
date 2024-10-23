from agency_swarm import Agent
from .tools.outline_tool import OutlineTool

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Responsible for generating video ideas and creating outlines.",
            instructions="./instructions.md",
            tools=[OutlineTool],
            temperature=0.7,
            max_prompt_tokens=25000,
        )
