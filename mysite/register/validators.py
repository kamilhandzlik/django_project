from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator

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
        # Funkcja do sprawdzenia, czy hasło jest zbyt podobne do podanej wartości
        from difflib import SequenceMatcher
        return SequenceMatcher(a=password.lower(), b=value.lower()).quick_ratio() >= self.max_similarity

class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Hasło jest zbyt krótkie. Powinno zawierać co najmniej %(min_length)d znaków."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Twoje hasło musi zawierać co najmniej %(min_length)d znaków."
        ) % {'min_length': self.min_length}

class CustomCommonPasswordValidator:
    def validate(self, password, user=None):
        common_passwords = ["password", "12345678", "87654321", "admin123", "admin321", "qwertyui", "drowssap",
                            "nimda321",
                            "something", "zaq123wsx", "123456789", "Polska123", "11111111", "22222222", "33333333",
                            "44444444", "55555555", "66666666", "77777777", "88888888", "99999999",
                            "xxx69Pussydestroyer69xxx", "xxxPussydestroyerxxx", "xxxPussyDestroyerxxx", "XXX69XXX666",
                            "666XXX666", "xxx666xxx", "XXX666XXX", "69XXX69XXX"]  # Dodaj tutaj więcej powszechnych haseł
        if password.lower() in common_passwords:
            raise ValidationError(
                _("Hasło jest zbyt powszechne."),
                code='password_too_common',
            )

    def get_help_text(self):
        return _("Twoje hasło nie może być powszechnie używane.")

class CustomNumericPasswordValidator:
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("Hasło nie może być całkowicie numeryczne."),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _("Twoje hasło nie może składać się wyłącznie z cyfr.")
