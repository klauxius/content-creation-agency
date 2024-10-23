from agency_swarm.tools import BaseTool
from pydantic import Field
from elevenlabs import generate, save
import os
from dotenv import load_dotenv

load_dotenv()

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

class CreateVoiceover(BaseTool):
    """
    A tool for creating a voiceover using the Eleven Labs TTS API.
    """
    text: str = Field(..., description="The text to be converted to speech.")
    voice_id: str = Field(default="21m00Tcm4TlvDq8ikWAM", description="The ID of the voice to use for the voiceover.")
    output_path: str = Field(..., description="The path to save the generated audio file.")

    def run(self):
        """
        Generates a voiceover using Eleven Labs TTS API and saves it to the specified path.
        """
        try:
            audio = generate(
                text=self.text,
                voice=self.voice_id,
                api_key=ELEVEN_LABS_API_KEY
            )
            save(audio, self.output_path)
            return f"Voiceover created and saved to: {self.output_path}"
        except Exception as e:
            return f"Error creating voiceover: {str(e)}"

if __name__ == "__main__":
    tool = CreateVoiceover(text="Hello, this is a test voiceover.", output_path="test_voiceover.mp3")
    print(tool.run())
