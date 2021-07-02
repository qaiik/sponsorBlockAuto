from youtube_transcript_api import YouTubeTranscriptApi

t = YouTubeTranscriptApi.get_transcript("QTk8Lx_Lpsk")

for key in t:
  if 'sponsor' in dict[key]['text']:
    print(dict[key]['text'])
