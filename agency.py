from agency_swarm import Agency
from content_manager.content_manager import ContentManager
from scriptwriter.scriptwriter import Scriptwriter
from video_producer.video_producer import VideoProducer

content_manager = ContentManager()
scriptwriter = Scriptwriter()
video_producer = VideoProducer()

agency = Agency([
    content_manager,  # Content Manager will be the entry point for communication with the user
    [content_manager, scriptwriter],  # Content Manager can initiate communication with Scriptwriter
    [scriptwriter, video_producer],   # Scriptwriter can initiate communication with Video Producer
],
    shared_instructions='agency_manifesto.md',
    temperature=0.7,
    max_prompt_tokens=25000
)

if __name__ == "__main__":
    agency.run_demo()
