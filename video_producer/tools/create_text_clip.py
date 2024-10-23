from agency_swarm.tools import BaseTool
from pydantic import Field
from moviepy.editor import TextClip
import os
from dotenv import load_dotenv

load_dotenv()

class CreateTextClip(BaseTool):
    """
    A tool for creating a text clip using moviepy.
    """
    text: str = Field(..., description="The text to display in the clip.")
    font_size: int = Field(default=70, description="The font size of the text.")
    color: str = Field(default="white", description="The color of the text.")
    bg_color: str = Field(default="transparent", description="The background color of the text clip.")
    duration: float = Field(..., description="The duration of the text clip in seconds.")

    def run(self):
        """
        Creates a text clip and returns its filename.
        """
        try:
            clip = TextClip(self.text, fontsize=self.font_size, color=self.color, bg_color=self.bg_color)
            clip = clip.set_duration(self.duration)
            filename = f"text_clip_{self.text[:10]}_{self.duration}.mp4"
            clip.write_videofile(filename, fps=24)
            return f"Text clip created: {filename}"
        except Exception as e:
            return f"Error creating text clip: {str(e)}"

if __name__ == "__main__":
    tool = CreateTextClip(text="Hello, World!", duration=3.0)
    print(tool.run())
