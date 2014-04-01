def get_beat_tuples(beats):
    return [(t.start, t.duration) for t in beats]

def match_beat_length(t1, t2):
	if len(t1.analysis.beats) == len(t2.analysis.beats):
		return (t1, t2), (t1.analysis.beats,t2.analysis.beats)
	(s_beats, s_track) = (t1.analysis.beats,t1) if len(t1.analysis.beats) < len(t2.analysis.beats) else (t2.analysis.beats,t2)
	(l_beats, l_track) = (t1.analysis.beats,t1) if len(t1.analysis.beats) > len(t2.analysis.beats) else (t2.analysis.beats,t2)
	tracks, beats = (s_track, l_track), (s_beats, l_beats[:len(s_beats)])
	return tracks, beats
