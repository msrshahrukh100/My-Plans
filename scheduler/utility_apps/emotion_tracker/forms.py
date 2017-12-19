from django import forms
from .models import EmotionJournal

class EmotionJournalForm(forms.ModelForm):


	def __init__(self, *args, **kwargs):
		super(EmotionJournalForm, self).__init__(*args, **kwargs)
		# self.fields['emotions_before'].widget.attrs['class'] = 'col l6 m10 s12 offset-l3 offset-m1'
		self.fields['situation'].widget.attrs['class'] = 'materialize-textarea'
		# self.fields['emotions_after'].widget.attrs['class'] = 'col l6 m10 s12 offset-l3 offset-m1'

	class Meta:
		model = EmotionJournal
		fields = ['emotions_before', 'situation', 'emotions_after']

