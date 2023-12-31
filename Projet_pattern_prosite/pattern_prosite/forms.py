from django import forms

# Reste d'un test pour upload les fichiers d'entrées mais pas fonctionnels en l'état.
# class UploadFileForm(forms.Form):
#     multifasta = forms.FileField(label='Multifasta')
#     sequence = forms.FileField(label='sequence')

class FilePathForm(forms.Form):
    multifasta_path = forms.CharField(label='Chemin du fichier multifasta')
    sequence_path = forms.CharField(label='Chemin du fichier sequence')
    seuil = forms.IntegerField(label='Seuil')
