from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.email.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'INFO',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'alchemy.accounts.models': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}
