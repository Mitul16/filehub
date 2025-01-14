from django.forms import ModelForm

from files.models import Directory, File


class FileForm(ModelForm):
    class Meta:
        model = File
        exclude = ["owner"]


class FileUpdateForm(ModelForm):
    class Meta:
        model = File
        fields = ["name"]


class DirectoryForm(ModelForm):
    class Meta:
        model = Directory
        fields = "__all__"


class DirectoryUpdateForm(ModelForm):
    class Meta:
        model = Directory
        fields = ["name"]
