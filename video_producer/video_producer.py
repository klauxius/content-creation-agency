from agency_swarm import Agent
from .tools.create_background import CreateBackground
from .tools.create_text_clip import CreateTextClip
from .tools.create_video_background import CreateVideoBackground
from .tools.add_audio import AddAudio
from .tools.export_video import ExportVideo
from .tools.create_voiceover import CreateVoiceover

class VideoProducer(Agent):
    def __init__(self):
        super().__init__(
            name="Video Producer",
            description="Responsible for producing videos using various tools.",
            instructions="./instructions.md",
            tools=[CreateBackground, CreateTextClip, CreateVideoBackground, AddAudio, ExportVideo, CreateVoiceover],
            temperature=0.7,
            max_prompt_tokens=25000,
        )
