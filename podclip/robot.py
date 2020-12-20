from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

@dataclass
class RobotState:
  pass

class Robot(metaclass=ABCMeta):
  
  @abstractmethod
  def run(state: RobotState) -> RobotState: pass