import mimetypes

from django.conf import settings

from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat
from rest_framework import status
from rest_framework.exceptions import ValidationError


@deconstructible
class FileValidator(object):
    error_messages = {
        'max_size': ("Ensure this file size is not greater than {}s."
                     " Your file size is {}s."),
        'content_type': "Files of type {}s are not supported. "
                        "Supported formats: txt or csv",
    }

    def __init__(self):
        self.max_size = settings.STUDYFILE_MAX_SIZE
        self.content_types = settings.STUDYFILE_ALLOWED_TYPES

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            raise ValidationError(
                detail=self.error_messages['max_size'].format(
                    filesizeformat(self.max_size),
                    filesizeformat(data.size)
                ),
                code=status.HTTP_400_BAD_REQUEST
            )

        if self.content_types:
            content_type = mimetypes.guess_type(data.name)[0]
            if self.content_types and not content_type in self.content_types:
                raise ValidationError(
                    detail=self.error_messages['content_type'].format(
                        str(content_type)
                    ),
                    code=status.HTTP_400_BAD_REQUEST
                )

    def __eq__(self, other):
        return (
                isinstance(other, FileValidator) and
                self.max_size == other.max_size and
                self.content_types == other.content_types
        )
