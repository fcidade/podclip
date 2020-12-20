from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

@dataclass
class RobotState:
  video_path: str # In
  clip_start: str # In
  clip_end: str   # In
  clip_path: str  # Out

class Robot(metaclass=ABCMeta):
  
  @abstractmethod
  def run(state: RobotState) -> RobotState: pass