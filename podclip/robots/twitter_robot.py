from podclip.robot import Robot, RobotState

class TwitterRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Posting to Twitter...')
    return state