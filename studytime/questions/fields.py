from collections import OrderedDict

from django import forms
from django.contrib.postgres.fields import ArrayField
from django.forms import SelectMultiple
from django.utils.encoding import force_text

from django_select2.forms import Select2TagWidget


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


class ArrayFieldWidget(Select2TagWidget):

    def render_options(self, *args, **kwargs):
        try:
            selected_choices, = args
        except ValueError:  # Signature contained `choices` prior to Django 1.10
            choices, selected_choices = args
        output = ['<option></option>' if not self.is_required and not self.allow_multiple_selected else '']
        selected_choices = {force_text(v) for v in selected_choices.split(',')}
        choices = {('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')}
        for option_value, option_label in choices:
            output.append(self.render_option(selected_choices, option_value, option_label))
        return '\n'.join(output)

    def value_from_datadict(self, data, files, name):
        values = super().value_from_datadict(data, files, name)
        return ",".join(values)
