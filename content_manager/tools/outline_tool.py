from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv

load_dotenv()

class OutlineTool(BaseTool):
    """
    A tool for writing and editing video outlines in markdown format and saving them locally.
    """
    content: str = Field(..., description="The content of the video outline in markdown format.")
    filename: str = Field(..., description="The filename to save the outline, including .md extension.")

    def run(self):
        """
        Writes the outline content to a markdown file and saves it locally.
        """
        try:
            with open(self.filename, 'w') as file:
                file.write(self.content)
            return f"Outline successfully saved to {self.filename}"
        except Exception as e:
            return f"Error saving outline: {str(e)}"

if __name__ == "__main__":
    tool = OutlineTool(content="# Video Title\n\n## Introduction\n\n## Main Points\n\n1. Point 1\n2. Point 2\n3. Point 3\n\n## Conclusion", filename="test_outline.md")
    print(tool.run())
