from podclip.robot import Robot, RobotState
import speech_recognition as sr
import logging

class SpeechRecognizerRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info(f'Extracting text from "{state.clip_audio_path}" in {state.language}')

    recognizer = sr.Recognizer()

    # FIXME: slipts and append: recognize in blocks of 60s to keep api from throwing
    with sr.AudioFile(state.clip_audio_path) as src:
      audio_file = recognizer.record(src, duration=60)

    # TODO: Fallback system
    result = recognizer.recognize_google(audio_file, language=state.language, show_all=False)
    state.clip_audio_transcription = result
    print(result)

    logging.info(f'Text result: "{result}"')
    return state