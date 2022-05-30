from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image_bin = image.binarisation(S)
    image_localisee = image_bin.localisation()
    max_similitude = 0
    liste_similitude = []
    for i in range(len(liste_modeles)):
         liste_similitude.append(image_localisee.similitude(liste_modeles[i]))
    for i in range(len(liste_similitude)):
        if liste_similitude[i] > max_similitude:
            max_similitude = liste_similitude[i]
            indice = i
    return indice
        
