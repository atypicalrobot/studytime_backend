from django import forms
from django.contrib.postgres.fields import ArrayField

from django.forms import SelectMultiple


class ArraySelectMultiple(SelectMultiple):

    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        try:
            getter = data.getlist
        except AttributeError:
            getter = data.get
        return getter(name)

    def value_omitted_from_data(self, data, files, name):
        # An unselected <select multiple> doesn't appear in POST data, so it's
        # never known if the value is actually omitted.
        return False


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of checkboxes.
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.SelectMultiple,
            'choices': self.base_field.choices,
            'coerce': self.base_field.to_python,
            'widget': ArraySelectMultiple,
        }
        defaults.update(kwargs)
        # skip formfield from parent class
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)
