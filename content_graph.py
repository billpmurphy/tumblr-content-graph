import collections
import json
import re
import sys
import time

import graphviz
import pytumblr


def get_user_post_sources(client, blogname):
    offset = 0
    total_posts = 1
    while offset < total_posts:
        time.sleep(1) # wait before each request to avoid being rate-limited

        posts = client.posts(blogname, offset=offset)
        total_posts = posts['total_posts']
        offset += len(posts['posts'])

        for post in posts['posts']:
            if 'source_title' in post:
                yield post['source_title']
    return


def get_top_n_sources(client, blogname, n):
    is_tumblr_source = lambda x: bool(re.match('^[A-Za-z0-9\-]+$', str(x)))
    sources = get_user_post_sources(client, blogname)
    sources = (s for s in sources if is_tumblr_source(s) and s != blogname)
    return collections.Counter(sources).most_common(n)


def build_graph(client, graph, blogname, num_sources, depth):
    for source, n_posts in get_top_n_sources(client, blogname, num_sources):
        graph.node(source)
        graph.edge(blogname, source, str(n_posts))
        if depth > 1:
            build_graph(client, graph, source, num_sources, depth-1)
    return


def main():
    blogname = sys.argv[1]
    num_sources = int(sys.argv[2])
    depth = int(sys.argv[3])
    filename = sys.argv[4]

    # load tumblr auth from file
    with open('tumblr_config.json', 'rb') as f:
        conf = json.loads(f.read())

    client = pytumblr.TumblrRestClient(
        conf['consumer_key'],
        conf['consumer_secret'],
        conf['oauth_token'],
        conf['oauth_secret']
    )

    # build the graph
    graph = graphviz.Digraph(format='svg')
    build_graph(client, graph, blogname, num_sources, depth)

    # style the graph
    graph.graph_attr.update({'fontcolor': 'white', 'bgcolor': '#333333',
                             'rankdir': 'BT', 'fontsize': '12'})
    graph.node_attr.update({'fontname': 'Helvetica', 'shape': 'hexagon',
                            'fontcolor': 'white', 'color': 'white',
                            'style': 'filled', 'fillcolor': '#006699',
                            'fontsize': '14'})
    graph.edge_attr.update({'style': 'dashed', 'color': 'white',
                            'arrowhead': 'open', 'fontname': 'Courier',
                            'fontsize': '12', 'fontcolor': 'white'})
    graph.render(filename)
    return


if __name__ == '__main__':
    main()
