<h1>AUTOMASH</h1>

automash is an automatic mashup generator. It uses your mood as an origin to source the songs and create an original, one-of-a-kind, mashup.

<h2>Installation</h2>

`git clone https://github.com/meg2208/automash.git`

`cd automash`

- Get an Echo Nest API key <a target="_blank" href="https://developer.echonest.com/account/register">here</a>

- enter the key at config.ECHO_NEST_API_KEY

`pip install -r requirements.txt`


<h2>Usage</h2>

`python make_mashup.py <mood> <output_name>`

so something like...

`python make_mashup.py bouncy bouncy_mashup.mp3`


<h2>Examples</h2>

<object height="45" width="167" type="application/x-shockwave-flash" id="audioPalPlayer" data="http://content.oddcast.com/host/audiopal/swf/workshop_player_shell.swf?mId=59322241.1&doorId=427&ds=http://host-d.oddcast.com/&playOnLoad=true&polFreq=&polUnit=">
	<param name="movie" value="http://content.oddcast.com/host/audiopal/swf/workshop_player_shell.swf?mId=59322241.1&doorId=427&ds=http://host-d.oddcast.com/&playOnLoad=true&polFreq=&polUnit=" />
	<param name="allowscriptaccess" value="always" />
	<param name="allownetworking" value="all" />
	<param name="base" value="/swf/" />
	<param name="quality" value="high" />
	<param name="bgcolor" value="#e8e9e3" />
	<param name="height" value="45" />
	<param name="width" value="167" />
	<param name="wmode" value="transparent" />
</object>



