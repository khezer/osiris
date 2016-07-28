def includeme(config):
    # Front page routes
    config.add_route('frontpage', '/')

    # Scan core app
    config.scan()
