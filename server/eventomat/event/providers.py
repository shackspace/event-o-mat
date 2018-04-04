from django.conf import settings
from social_core.backends.gitlab import GitLabOAuth2


class ShackGitLabOAuth2(GitLabOAuth2):
    name = 'shackgitlab'
    API_URL = 'https://git.shackspace.de'
    AUTHORIZATION_URL = 'https://git.shackspace.de/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://git.shackspace.de/oauth/token'


def end_pipeline(strategy, details, user=None, *args, **kwargs):
    url = 'http://localhost:8880/' if settings.DEBUG else 'http://events.shackspace.de/'
    url = f'{url}#token={user.auth_token.key}'
    return strategy.redirect(url)
