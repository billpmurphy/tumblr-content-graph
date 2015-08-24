One cool thing you can do with Tumblr's REST API is see where content on a
particular Tumblr blog originally came from. This repository contains a tool
for doing just that.

`content_graph.py` will find the original author of all reblogged posts on a
particular blog and turn the result into a dependency tree diagram.

**Usage:**

1) Get your Tumblr API credentials and stash them in a JSON file, `tumblr_conf.json`.

2) Make sure you have [graphviz](http://www.graphviz.org) installed and in your
`$PATH`.

3) Finally, run `content_graph.py`.

```
python content_graph.py <blog> <leaves_per_node> <tree_max_depth> <output_filename>
```
