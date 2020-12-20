from podclip.robot import Robot, RobotState
import moviepy.editor as mp
import logging

class AudioExtractorRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info(f'Converting video "{state.clip_path}" to audio...')

    mp.VideoFileClip(state.clip_path).audio.write_audiofile(state.clip_audio_path)

    logging.info(f'Audio file seved on "{state.clip_audio_path}"!')
    return state