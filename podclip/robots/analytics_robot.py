from podclip.robot import Robot, RobotState

class AnalyticsRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Analyzing...')
    return state