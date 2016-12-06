from pymongo import MongoClient
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.events import NewRequest
from osiris.locale import _

_ = _  # PyFlakes


def emulate_http(config):
    """ Add compatibllity Backbone emulate_http method with cornice
    """
    def backbone_emulate_http(event):
        if event.request.method == 'POST':
            method = event.request.json.get('_method')
            # method = event.request.headers.get('X-HTTP-Method-Override', '')
            if method is not None:
                event.request.method = method.upper()

    # Add compatibllity Backbone emulate_http method with cornice
    config.add_subscriber(backbone_emulate_http, NewRequest)

    # Disable cornice handle_exceptions
    # https://github.com/mozilla-services/cornice/issues/183
    config.add_settings(handle_exceptions=False)

    # Include cornice RESTful API
    config.include('cornice')


def database(config):
    """ Connect to MongoDB database
    """
    def mongodb_connect(event):
        settings = event.request.registry.settings
        if 'mongodb.uri' in settings:
            mongo_client = MongoClient(settings['mongodb.uri'])
            event.request.db = mongo_client[settings['mongodb.db']]
        else:
            event.request.db = None

    # Connect to MongoDB database
    config.add_subscriber(mongodb_connect, NewRequest)


def locale(config):
    # Add translation directory
    config.add_translation_dirs('osiris:locale/')

    def locale_direction(request):
        direction = 'ltr'
        if request.locale_name in ['fa', 'ar']:
            direction = 'rtl'
        return direction

    # Add locale_dir property in request
    config.set_request_property(locale_direction, 'locale_dir', reify=True)


def auth(config):
    # Security policies
    settings = config.get_settings()
    authn_policy = AuthTktAuthenticationPolicy(
        settings['auth_secret'],
        cookie_name=settings['cookie_name'],
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)


def static(config):
    config.add_static_view(
        'osiris/static', 'osiris:static', cache_max_age=3600)


def template(config):
    config.include('pyramid_layout')
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')


def includeme(config):
    """ This function include osiris package configuration.
    """

    # Emulate http request
    config.include(emulate_http)

    # Database connection config
    config.include(database)

    # Locale and Translation configuration
    config.include(locale)

    # Authentication and Authorization Policy
    config.include(auth)

    # Static location and configuration
    config.include(static)

    # Template location and configuration
    config.include(template)

    # Scan osiris  package folder
    config.scan(package='osiris')
