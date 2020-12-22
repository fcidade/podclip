from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

@dataclass
class RobotState:
  youtube_url:              str = field(default='')       # Video URL

  video_path:               str = field(default='')       # Video path
  clip_start:               int = field(default=0)        # In seconds
  clip_end:                 int = field(default=0)        # In seconds
  clip_path:                str = field(default='')       # Video path

  clip_audio_path:          str = field(default='')       # Audio path
  language:                 str = field(default='')       # Audio language
  clip_audio_transcription: str = field(default='')       # Audio transcription

  thumb_frame:              str = field(default='')       # Image path
  thumb_quote:              str = field(default='')       # Best quote
  thumb_path:               str = field(default='')       # Image path

class Robot(metaclass=ABCMeta):
  
  @abstractmethod
  def run(state: RobotState) -> RobotState: pass