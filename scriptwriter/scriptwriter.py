from agency_swarm import Agent

class Scriptwriter(Agent):
    def __init__(self):
        super().__init__(
            name="Scriptwriter",
            description="Responsible for writing full scripts based on video outlines.",
            instructions="./instructions.md",
            tools=[],
            temperature=0.7,
            max_prompt_tokens=25000,
        )
