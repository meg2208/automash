# encoding: utf=8
from scripts.file_retrieval import get_file
from config import ECHO_NEST_API_KEY
from pyechonest import config
config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY
from pyechonest.song import search as song_search
import echonest.remix.audio as audio
from echonest.remix.action  import Crossmatch
import urllib2
import time
from random import shuffle
from common import VALID_MOODS, PARTIAL_MASHUP_DIR, OUTPUT_DIR
from helpers import get_beat_tuples, match_beat_length
from scripts.file_retrieval import get_file

class MoodBoombox(object):

	def __init__(self, mood=None, output_name=None):
		start = time.time()
		if not mood:
			raise Exception("NO MOOD SPECIFIED")
		elif not output_name:
			raise Exception("Please specify a file output name")
		elif mood not in VALID_MOODS:
			raise Exception("Invalid mood: {}".format(mood))
		self.output_name = output_name
		self.mood = mood
		self.lead_track = {'sample_url': '', 'local_url': ''}
		self.other_tracks = {'sample_urls': [], 'local_urls': []}
		self.other_track_urls = []
		self.run()
		end = time.time()
		print 'that took {}'.format(end-start)
		
	def run(self):
		self.set_lead_track()
		self.set_other_track()
		self.set_other_track()
		self.make_song()

	def set_lead_track(self):
		track_url = self.get_track('lead', mood=self.mood, min_speechiness=0.5, 
		  min_danceability=0.6, buckets=['id:7digital-US', 'tracks'], results=6)
		local_url = get_file(track_url)
		self.lead_track['sample_url'] = track_url
		self.lead_track['local_url'] = local_url

	def set_other_track(self):
		track_url = self.get_track('other', mood=self.mood, max_speechiness=0.3, 
		  min_danceability=0.8, buckets=['id:7digital-US', 'tracks'], results=7)
		local_url = get_file(track_url)
		self.other_tracks['local_urls'].append(local_url)
		self.other_tracks['sample_urls'].append(track_url)

	def get_track(self, search_type, **song_preferences):
		if search_type == 'other' and self.other_track_urls:
			track_urls = self.other_track_urls
		else:
			results = song_search(**song_preferences)
			shuffle(results)
			track_urls = [s.get_tracks("7digital-US")[0].get("preview_url") for s in results\
			 					if s.get_tracks("7digital-US") and 							\
			 					 s.get_tracks("7digital-US")[0].get("preview_url")]
			self.other_track_urls = track_urls if search_type == 'other' else self.other_track_urls
		for url in track_urls:
			try:
				urllib2.urlopen(url)
			except:
				continue
			else:
				if url not in [self.lead_track['sample_url']]+self.other_tracks['sample_urls']:
					return url
				else:
					continue
		# if we got this far, then you got no tracks for the request
		raise Exception("We either didn't get enough results for that mood or the urls for the song samples were faulty")

	# "crossmatch" the two other tracks 
	# then crossmatch the result w the lead
	def make_song(self, t1_url=None, t2_url=None, is_lead=False):
		def local(u):
			return u if len(u.split("/")) > 1 and "temp__" in u.split("/")[1] else PARTIAL_MASHUP_DIR+u

		if not t1_url and not t2_url:
			t1_url, t2_url = tuple(self.other_tracks['local_urls'])
		t1, t2 = audio.LocalAudioFile(local(t1_url)), audio.LocalAudioFile(local(t2_url))
		mashup = Mashup('crossmatch', t1, t2)
		out = mashup.process_tracks()
		if not is_lead:
			file_name = "{dir}temp__{name}.mp3".format(dir=OUTPUT_DIR, name=self.output_name)
			out.encode(file_name)
			self.make_song(t1_url=file_name, t2_url=self.lead_track['local_url'], is_lead=True)
		else:
			out.encode("{dir}{name}.mp3".format(dir=OUTPUT_DIR, name=self.output_name))


class Mashup(object):

	accepted_methods = ['crossmatch']

	def __init__(self, method, *tracks):
		self.method = method
		for i,track in enumerate(tracks):
			setattr(self,'t{}'.format(i+1), track)

	def process_tracks(self):
		if self.method == "crossmatch":
			tracks, _beats = match_beat_length(self.t1, self.t2)
			beats = (get_beat_tuples(_beats[0]), get_beat_tuples(_beats[1]))
			cm = Crossmatch(tracks, beats)
			return cm.render()
		elif method not in accepted_methods:
			raise Exception("You must use one of these valid methods: {}".format(', '.join(accepted_methods)))


