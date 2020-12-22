from podclip.robot import Robot, RobotState
import logging

class UserInputRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info('Receiving input from user...')

    print('Hi! I need some info to generate your clip! :D')

    state.video_path = self.input('Video URL')
    state.video_path = self.input('Path to save video')
    state.clip_path = self.input('Path to save clip')
    state.clip_start = self.input('Clip start (in seconds)')
    state.clip_end = self.input('Clip end (in seconds)')
    state.thumb_path = self.input('Path to save thumbnail')
    state.thumb_frame = self.input('Clip frame for thumbnail')
    state.thumb_quote = self.input('Quote for thumbnail')

    print('Thanks! :)')

    return state

  def input(self, msg: str):
    return input(f'{msg.strip()}: ')