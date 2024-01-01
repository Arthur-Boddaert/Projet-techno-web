from django.shortcuts import render
from .forms import FilePathForm
from boddaert_patternprosite import pratt_fonction

# Create your views here.
def formulaire(request):
    if request.method == 'POST':
        form = FilePathForm(request.POST)
        if form.is_valid():
            multifasta_path = form.cleaned_data['multifasta_path']
            sequence_path = form.cleaned_data['sequence_path']
            seuil = form.cleaned_data['seuil']

            pattern, occurence = pratt_fonction.patternprosite(multifasta_path, sequence_path, seuil)
            conserver = pratt_fonction.verif_conserv(multifasta_path)
            indel = pratt_fonction.verif_indel(multifasta_path)
            if indel is not None:
                nb_seq_indel = len(indel)
                indel = f'Les séquences suivantes contiennent des indels : {indel}'
            else:
                nb_seq_indel = 0
                indel = 'Les séquences du fichier FASTA ne contiennent pas d\'indels'
            if conserver is not None:
                nb_conserv = len(conserver)
                conserver = f'Les sites suivant sont conservés : { conserver }'
            else:
                nb_conserv = 0
                conserver = 'Aucuns des sites n\'est conservés'
            nb_seq, taille = pratt_fonction.info_rapide(multifasta_path)
            return render(request, 'resultat.html', {'pattern': pattern, 'occurence': occurence,
                          'conserver': conserver, 'indel': indel, 'nb_conserv': nb_conserv, 'nb_seq_indel': nb_seq_indel,
                            'nb_seq': nb_seq, 'taille': taille})
    else:
        form = FilePathForm()

    return render(request, 'formulaire.html', {'form': form})