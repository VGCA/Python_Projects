#pip install moviepy

import moviepy.editor
import sys

videoFileClip = moviepy.editor.VideoFileClip(sys.argv[1]);
ext_audio = videoFileClip.audio
ext_audio.write_audiofile('extracted.mp3')