from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['1c.png','2c.png','10c.png','20c.png','50.png','1e.png', 
            '2e.png']
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
        