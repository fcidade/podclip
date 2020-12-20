from podclip.robot import Robot, RobotState

class TittleRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Generating Title...')
    return state