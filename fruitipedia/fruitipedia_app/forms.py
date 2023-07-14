from django import forms
from fruitipedia.fruitipedia_app.models import Profile, Fruit


class ProfileForm(forms.ModelForm):
    """Form for the Profile model"""

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False

    class Meta:
        model = Profile
        exclude = ('image_url', 'age',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'render_value': False}),
        }


class ProfileDeleteForm(forms.ModelForm):
    """Form for the Profile model"""

    def save(self, commit=True):
        profile = self.instance
        profile.delete()
        return profile

    class Meta:
        model = Profile
        fields = ()


class FruitForm(forms.ModelForm):
    """Form for the Fruit model"""

    def __init__(self, *args, **kwargs):
        super(FruitForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False

    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitDeleteForm(forms.ModelForm):
    """Form for the Fruit model"""

    class Meta:
        model = Fruit
        exclude = ('nutrition',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
        }

