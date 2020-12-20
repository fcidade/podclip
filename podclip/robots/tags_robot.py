from podclip.robot import Robot, RobotState

class TagsRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Generating Tags...')
    return state