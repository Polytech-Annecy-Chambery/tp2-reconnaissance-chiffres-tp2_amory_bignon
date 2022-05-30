from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W,_ = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #=========================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #=========================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j].any() <= S:
                    im_bin.pixels[i][j] = 0
                else:
                    im_bin.pixels[i][j] = 255
        return im_bin


    #=========================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #=========================================================================
    def localisation(self):
        # im_bin = self.binarisation(self, S=128)
        im_recadree = Image()
        L_min, L_max = self.H, 0
        C_min, C_max = self.W, 0
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j] == 0:
                    if i < L_min:
                        L_min = i
                    if i > L_max:
                        L_max = i
                    if j < C_min:
                        C_min = j
                    if j > C_max:
                        C_max = j
        im_recadree.set_pixels(self.pixels[L_min:L_max+1, C_min:C_max+1])
                    
        return im_recadree

    #=========================================================================
    # Methode de redimensionnement d'image
    #=========================================================================
    def resize(self, new_H, new_W):
        im_resized = Image()
        pix_resized = resize(self.pixels, (new_H,new_W), 0)
        pix_resized_int = np.uint8(pix_resized*255)
        im_resized.set_pixels(pix_resized_int)
        return im_resized



    #=========================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #=========================================================================
    def similitude(self, im):
        image_resize=self.resize(im.H, im.W)
        pix_semblables = 0
        pix1 = im.pixels
        pix2 = image_resize.pixels
        for i in range(image_resize.H):
            for j in range(image_resize.W):
                if pix1[i][j] == pix2[i][j]:
                    pix_semblables += 1
        return pix_semblables/(image_resize.H * image_resize.W)
                    

