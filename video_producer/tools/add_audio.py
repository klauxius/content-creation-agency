from agency_swarm.tools import BaseTool
from pydantic import Field
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import os
from dotenv import load_dotenv

load_dotenv()

class AddAudio(BaseTool):
    """
    A tool for adding audio to a video clip using moviepy.
    """
    video_path: str = Field(..., description="The path to the input video file.")
    audio_path: str = Field(..., description="The path to the audio file to be added.")
    output_path: str = Field(..., description="The path for the output video file with added audio.")

    def run(self):
        """
        Adds audio to the video and returns the output filename.
        """
        try:
            video = VideoFileClip(self.video_path)
            audio = AudioFileClip(self.audio_path)
            
            video_duration = video.duration
            audio_duration = audio.duration
            
            if audio_duration < video_duration:
                audio = audio.loop(duration=video_duration)
            else:
                audio = audio.subclip(0, video_duration)
            
            final_clip = CompositeVideoClip([video.set_audio(audio)])
            final_clip.write_videofile(self.output_path, fps=24)
            
            return f"Video with added audio created: {self.output_path}"
        except Exception as e:
            return f"Error adding audio to video: {str(e)}"

if __name__ == "__main__":
    tool = AddAudio(video_path="input_video.mp4", audio_path="input_audio.mp3", output_path="output_video_with_audio.mp4")
    print(tool.run())
