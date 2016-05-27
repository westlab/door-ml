import toml

conf = {}

def parse_conf(fpath):
    with open(fpath) as f:
        conf = toml.loads(f.read())
    return conf
