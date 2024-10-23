from agency_swarm.tools import BaseTool
from pydantic import Field
from moviepy.editor import ColorClip
import os
from dotenv import load_dotenv

load_dotenv()

class CreateBackground(BaseTool):
    """
    A tool for creating a solid color background clip using moviepy.
    """
    color: str = Field(..., description="The color of the background (e.g., 'red', '#FF0000').")
    duration: float = Field(..., description="The duration of the background clip in seconds.")
    size: tuple = Field(default=(1920, 1080), description="The size of the background clip in pixels (width, height).")

    def run(self):
        """
        Creates a solid color background clip and returns its filename.
        """
        try:
            clip = ColorClip(size=self.size, color=self.color, duration=self.duration)
            filename = f"background_{self.color}_{self.duration}.mp4"
            clip.write_videofile(filename, fps=24)
            return f"Background clip created: {filename}"
        except Exception as e:
            return f"Error creating background clip: {str(e)}"

if __name__ == "__main__":
    tool = CreateBackground(color="blue", duration=5.0)
    print(tool.run())
