
import logging
log = logging.getLogger('django')

from django.conf import settings as django_settings

from celery.signals import task_failure


def register_signal():
    def process_failure_signal(
            sender, task_id, exception,
            traceback, einfo, args, kwargs, **kw):
        # This signal is fired inside the stack so let raven do its magic
        log.warning(str(einfo))
        einfo = str(einfo)
        django_settings.MYRAVEN_CONFIG['exception_handler'](einfo)

    log.info('register_signal success')

    task_failure.connect(process_failure_signal, weak=False)