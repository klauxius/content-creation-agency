from agency_swarm.tools import BaseTool
from pydantic import Field
from moviepy.editor import VideoFileClip
import os
from dotenv import load_dotenv

load_dotenv()

class CreateVideoBackground(BaseTool):
    """
    A tool for creating a video background from an existing video file.
    """
    video_path: str = Field(..., description="The path to the input video file.")
    duration: float = Field(..., description="The desired duration of the output video in seconds.")
    output_size: tuple = Field(default=(1920, 1080), description="The size of the output video (width, height).")

    def run(self):
        """
        Creates a video background and returns its filename.
        """
        try:
            clip = VideoFileClip(self.video_path)
            clip = clip.resize(self.output_size)
            if clip.duration < self.duration:
                clip = clip.loop(duration=self.duration)
            else:
                clip = clip.subclip(0, self.duration)
            
            output_filename = f"video_background_{os.path.basename(self.video_path)}"
            clip.write_videofile(output_filename, fps=24)
            return f"Video background created: {output_filename}"
        except Exception as e:
            return f"Error creating video background: {str(e)}"

if __name__ == "__main__":
    tool = CreateVideoBackground(video_path="input_video.mp4", duration=10.0)
    print(tool.run())
