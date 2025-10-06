from core import Formatter
from formatters import CloudWatchAlarm, IgnoreCreateServiceLinkedRole, IamChanges, SESBounces, IgnoreSESTransientBounces


class FormattersFactory(object):
    @staticmethod
    def formatter(formater: str) -> Formatter:
        if formater == "cloud_watch_alarm":
            return CloudWatchAlarm()
        if formater == "ignore_create_service_linked_role":
            return IgnoreCreateServiceLinkedRole()
        if formater == "iam_changes":
            return IamChanges()
        if formater == "ses_bounces":
            return SESBounces()
        if formater == "ses_ignore_transient_bounces":
            return IgnoreSESTransientBounces()
        return Formatter()
