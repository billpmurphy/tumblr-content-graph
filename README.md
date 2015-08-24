One cool thing you can do with Tumblr's REST API is see where content on a
particular Tumblr blog originally came from. This repository contains a tool
for doing just that.

`content_graph.py` will find the original author of all reblogged posts on a
particular blog and turn the result into a dependency tree diagram.

**Usage:**

1) Clone this repository and install the dependencies. Make sure you have
   [graphviz](http://www.graphviz.org) installed and in your `$PATH`.

```
git clone https://github.com/billpmurphy/tumblr-content-graph
cd tumblr-content-graph

virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

2) Get your Tumblr API credentials and stash them in a JSON file, `tumblr_conf.json`.

3) Finally, run `content_graph.py`.

```
python content_graph.py <blog> <leaves_per_node> <tree_max_depth> <output_filename>
```

For example:

```
python content_graph.py you-have-just-experienced-things 2 4 example
```

This generates the following graph:

![Example](../master/example.svg?raw=true)
