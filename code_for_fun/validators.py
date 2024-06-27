from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator,
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator
)
from difflib import SequenceMatcher


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def __init__(self, user_attributes=('username', 'email'), max_similarity=0.7):
        self.user_attributes = user_attributes
        self.max_similarity = max_similarity

    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue

            if self._password_too_similar(password, value):
                raise ValidationError(
                    _("Twoje hasło jest zbyt podobne do twoich innych danych osobowych."),
                    code='password_too_similar',
                )

    def get_help_text(self):
        return _("Twoje hasło nie może być podobne do twoich innych danych osobowych.")

    def _password_too_similar(self, password, value):
        return SequenceMatcher(a=password.lower(), b=value.lower()).quick_ratio() >= self.max_similarity


class CustomMinimumLengthValidator(MinimumLengthValidator):
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user):
        try:
            super().validate(password, user)
        except  ValidationError:
            raise ValidationError(
                _("Hasło jest zbyt krótkie. Powinno zawierać co najmniej %(min_length)d znaków."),
                code='password_too_short',
                params={'min_length': self.min_length},
        )

    def get_help_text(self):
        return _(
            "Twoje hasło musi zawierać co najmniej %(min_length)d znaków."
        ) % {'min_length': self.min_length}
class CustomCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user):
        try:
            super().validate(password, user=None)
        except ValidationError:
            raise ValidationError(
                _("Twoje hasło jest zbyt popularne. Proszę użyć trudniejszego hasła."),
                code='password_too_common',
            )

    def get_help_text(self):
        return _("Twoje hasło nie może być powszechnie używane.")

class CustomNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user):
        try:
            super().validate(password, user)
        except ValidationError:
            raise ValidationError(
                _("Hasło nie może być całkowicie numeryczne."),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _("Twoje hasło nie może składać się wyłącznie z cyfr.")