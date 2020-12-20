from podclip.robot import Robot, RobotState

class DescriptionRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Generating Description...')
    return state