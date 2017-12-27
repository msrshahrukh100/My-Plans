from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ExerciseForm, self).__init__(*args, **kwargs)
		# self.fields['emotions_before'].widget.attrs['class'] = 'col l6 m10 s12 offset-l3 offset-m1'
		self.fields['sets'].widget.attrs['class'] = 'col l6 m10 s12 offset-l3 offset-m1'
		# self.fields['emotions_after'].widget.attrs['class'] = 'col l6 m10 s12 offset-l3 offset-m1'

	class Meta:
		model = Exercise
		fields = ['sets', 'reps', 'max_weight']
