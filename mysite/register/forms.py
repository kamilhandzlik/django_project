from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_('Użytkownik'),
        help_text=_("Wymagania dla nazwy użytkownika. Maksymalnie 150 znaków. Tylko litery, cyfry i następujące znaki @/./+/-/_."),
        error_messages={
            'required': _('To pole jest wymagane.'),
            'invalid': _('Wprowadź poprawną nazwę użytkownika.'),
            'unique': _('Użytkownik o takiej nazwie już istnieje.')
        }
    )

    email = forms.EmailField(
        label=_('Email'),
        error_messages={
            'required': _('To pole jest wymagane.'),
            'invalid': _('Wprowadź poprawny adres email.')
        }
    )

    password1 = forms.CharField(
        label=_('Hasło'),
        widget=forms.PasswordInput,
        help_text=_(
            "<ul>"
            "<li>Twoje hasło nie może być podobne do twoich innych danych osobowych.</li>"
            "<li>Twoje hasło musi zawierać co najmniej 8 znaków.</li>"
            "<li>Twoje hasło nie może być powszechnie używane.</li>"
            "<li>Twoje hasło nie może składać się wyłącznie z cyfr.</li>"
            "</ul>"
        ),
        error_messages={
            'required': _("To pole jest wymagane."),
            'password_too_short': _("Hasło jest zbyt krótkie. Powinno zawierać co najmniej 8 znaków."),
            'password_common': _("Hasło jest zbyt powszechne."),
            'password_entirely_numeric': _("Hasło nie może być całkowicie numeryczne."),
        }
    )
    password2 = forms.CharField(
        label=_('Potwierdzenie hasła'),
        widget=forms.PasswordInput,
        help_text=_("Wprowadź to samo hasło, co powyżej, w celu weryfikacji."),
        error_messages={
            'required': _("To pole jest wymagane."),
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError(
                self.fields['password1'].error_messages['password_too_short'],
                code='password_too_short',
            )
        if password1.isdigit():
            raise forms.ValidationError(
                self.fields['password1'].error_messages['password_entirely_numeric'],
                code='password_entirely_numeric',
            )
        # Dodaj inne walidacje hasła tutaj, jeśli potrzebne

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Hasła nie pasują do siebie."))

        return password2
