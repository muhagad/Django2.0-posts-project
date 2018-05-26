from  django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def validate_domain_email_only(value):
    if "yourdomain.com" not in value:
        raise ValidationError(_("sorry, your EMail is not valid"))
    return value
