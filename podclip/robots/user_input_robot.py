from podclip.robot import Robot, RobotState
import logging

class UserInputRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info('Receiving input from user...')

    print('Hi! I need some info to generate your clip! :D')

    state.youtube_url = r'https://www.youtube.com/watch?v=oBoU12JN0QY&ab_channel=Podpah'
    state.video_path = r'./test/resources/videos/a deriva 6 - arthur petry.mp4'
    state.clip_path = r'./test/resources/videos/clip02.mp4'
    state.clip_start = 10
    state.clip_end = 40
    state.thumb_path = r'./test/resources/videos/thumb02.png'
    state.thumb_frame_path = r'./test/resources/videos/frame.png'
    state.thumb_quote = 'nice quote'

    # state.youtube_url = self.input('Video URL')
    # state.video_path = self.input('Path to save video')
    # state.clip_path = self.input('Path to save clip')
    # state.clip_start = self.input('Clip start (in seconds)')
    # state.clip_end = self.input('Clip end (in seconds)')
    # state.thumb_path = self.input('Path to save thumbnail')
    # state.thumb_frame_path = self.input('Clip frame for thumbnail')
    # state.thumb_quote = self.input('Quote for thumbnail')

    print('Thanks! :)')

    return state

  def input(self, msg: str):
    return input(f'{msg.strip()}: ')