from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

@dataclass
class RobotState:
  video_path: str # System path
  clip_start: int # In seconds
  clip_end: int   # In seconds
  clip_path: str  # System path

class Robot(metaclass=ABCMeta):
  
  @abstractmethod
  def run(state: RobotState) -> RobotState: pass