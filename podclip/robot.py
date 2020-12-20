from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

@dataclass
class RobotState:
  video_path:               str = field(default='')       # System path
  clip_start:               int = field(default=0)        # In seconds
  clip_end:                 int = field(default=0)        # In seconds
  clip_path:                str = field(default='')       # System path

  clip_audio_path:          str = field(default='')       # System path
  language:                 str = field(default='')       # Audio language
  clip_audio_transcription: str = field(default='')       # Audio transcription

class Robot(metaclass=ABCMeta):
  
  @abstractmethod
  def run(state: RobotState) -> RobotState: pass