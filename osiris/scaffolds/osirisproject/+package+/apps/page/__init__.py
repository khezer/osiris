def includeme(config):
    # Pages routes
    config.add_route('page', 'page/{slug}')

    # Scan page app
    config.scan()
