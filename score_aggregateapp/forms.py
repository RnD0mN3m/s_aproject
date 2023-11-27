from django.forms import ModelForm
from .models import ScoreAggregateappPost
class ScoreAggregateappPostForm(ModelForm):
    class Meta:
        model = ScoreAggregateappPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']