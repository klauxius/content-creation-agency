from agency_swarm.tools import BaseTool
from pydantic import Field
from moviepy.editor import VideoFileClip
import os
from dotenv import load_dotenv

load_dotenv()

class ExportVideo(BaseTool):
    """
    A tool for exporting a video file with specific settings using moviepy.
    """
    input_path: str = Field(..., description="The path to the input video file.")
    output_path: str = Field(..., description="The path for the output video file.")
    resolution: tuple = Field(default=(1920, 1080), description="The resolution of the output video (width, height).")
    fps: int = Field(default=24, description="The frames per second of the output video.")
    bitrate: str = Field(default="8000k", description="The bitrate of the output video.")

    def run(self):
        """
        Exports the video with specified settings and returns the output filename.
        """
        try:
            clip = VideoFileClip(self.input_path)
            clip = clip.resize(self.resolution)
            clip.write_videofile(self.output_path, fps=self.fps, bitrate=self.bitrate)
            return f"Video exported successfully: {self.output_path}"
        except Exception as e:
            return f"Error exporting video: {str(e)}"

if __name__ == "__main__":
    tool = ExportVideo(input_path="input_video.mp4", output_path="exported_video.mp4")
    print(tool.run())
