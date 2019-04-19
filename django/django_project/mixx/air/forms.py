from django import forms
import os

class TellForm(forms.Form):
    visitor = forms.CharField(label='您的姓名', max_length=20, required=True)
    email =forms.EmailField(label='E-Mail', max_length=30, required=True)
    content = forms.CharField(label='留言', max_length=200, widget=forms.Textarea, initial="我覺得...")
    
class GenForm(forms.Form):
    msg =forms.CharField(label='訊息', widget=forms.Textarea)
    font_size = forms.IntegerField(label='文字尺寸(12-80)', min_value=12, max_value=80)
    x = forms.IntegerField(label='X(0-50)', min_value=0, max_value=50)
    y = forms.IntegerField(label='Y(0-100)', min_value=0, max_value=100)
    
    """
    def __init__(self, backfiles, *args, **kwargs):
        super(GenForm, self).__init__(*args, **kwargs)
        self.fields['backfile']= forms.ChoiceField(
                choices=[(os.path.basename(bf), os.path.basename(bf)) for bf in backfiles])
    """
                
class UploadForm(forms.Form):
    file=forms.FileField()