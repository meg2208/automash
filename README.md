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

<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/142455002&amp;auto_play=false&amp;hide_related=false&amp;visual=true"></iframe>
