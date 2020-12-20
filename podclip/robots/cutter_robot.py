from podclip.robot import Robot, RobotState

class CutterRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Cutting...')
    return state