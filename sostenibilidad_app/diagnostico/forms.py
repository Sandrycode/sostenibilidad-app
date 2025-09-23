from django import forms
from .models import Diagnostico

OPCIONES_SI_NO = [
    ('true', 'Sí'),
    ('false', 'No'),
]

class DiagnosticoForm(forms.ModelForm):
    tiene_politica_ambiental = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    cumple_normativa_local = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    realiza_auditorias = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    gestiona_residuos = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    usa_energia_renovable = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    mide_consumo_agua = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    tiene_plan_emergencia = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    involucra_empleados = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    comunica_transparente = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    colabora_comunidad = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    promueve_igualdad = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )
    evalua_proveedores = forms.TypedChoiceField(
        choices=OPCIONES_SI_NO,
        widget=forms.RadioSelect,
        coerce=lambda x: x == 'true'
    )

    class Meta:
        model = Diagnostico
        fields = [
            'nombre_empresa',
            'sector',
            'tiene_politica_ambiental',
            'cumple_normativa_local',
            'realiza_auditorias',
            'gestiona_residuos',
            'usa_energia_renovable',
            'mide_consumo_agua',
            'tiene_plan_emergencia',
            'involucra_empleados',
            'comunica_transparente',
            'colabora_comunidad',
            'promueve_igualdad',
            'evalua_proveedores',
            'observaciones',
        ]
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Asignar los verbose_name del modelo como label
        for name, field in self.fields.items():
            field.required = True
            field.label = self._meta.model._meta.get_field(name).verbose_name
            if name == 'observaciones':
                field.required = False
                field.widget.attrs.pop('required', None)
            elif not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['id'] = f'id_{name}'
                field.widget.attrs['required'] = 'required'


from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'password-input', 'id': 'id_password1'})
        self.fields['password2'].widget.attrs.update({'class': 'password-input', 'id': 'id_password2'})



