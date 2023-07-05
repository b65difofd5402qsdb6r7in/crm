from django.db import models
from django.contrib.auth.models import AbstractUser


# 

class Signature(models.Model):
    signature_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Utilisateur(AbstractUser):
    FONCTIONS = (
        ('Administrateur', 'Administrateur'),
        ('Boss', 'Boss'),
        ('Commercial', 'Commercial'),
        ('Moderateur', 'Moderateur'),
        ('Webmaster', 'Webmaster')
    )

    fonction = models.CharField(choices=FONCTIONS, max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero_telephone = models.CharField(max_length=20)
    email = models.EmailField()


class Client(models.Model):
    STATUTS_JURIDIQUES = (
    ('SAS', 'SAS'),
    ('SARL', 'SARL'),
    ('SA', 'SA'),
    ('SASU', 'SASU'),
    ('EURL', 'EURL'),
    ('SCI', 'SCI'),
    ('SCOP', 'SCOP'),
    ('SNC', 'SNC'),
    ('GIE', 'GIE'),
)
    CIVILITES = (
    ('M', 'M'),
    ('Mme', 'Mme'),
    ('Mlle', 'Mlle'),
    ('Autre', 'Autre'),
)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    civilite = models.CharField(choices=CIVILITES, max_length=5, null=True)
    numero_telephone = models.CharField(max_length=20)
    email = models.EmailField()
    siret = models.CharField(max_length=14)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    nom_societe = models.CharField(max_length=100)
    statut_juridique = models.CharField(choices=STATUTS_JURIDIQUES ,max_length=5)
    commentaire = models.TextField() 
    responsable_commercial = models.ForeignKey("Utilisateur", on_delete=models.SET_DEFAULT, default="Non Assigne")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# class Utilisateur(models.Model):
#     FONCTIONS = (
#     ('Administrateur', 'Administrateur'),
#     ('Boss', 'Boss'),
#     ('Commercial', 'Commercial'),
#     ('Moderateur', 'Moderateur'),
#     ('Webmaster', 'Webmaster')
# )
#     utilisateur = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
#     fonction = models.CharField(choices=FONCTIONS ,max_length=50)
#     nom = models.CharField(max_length=50)
#     prenom = models.CharField(max_length=50)
#     numero_telephone = models.CharField(max_length=20)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.nom} {self.prenom}"


# class Client(models.Model):
    #     STATUTS_JURIDIQUES = (
#     ('SAS', 'SAS'),
#     ('SARL', 'SARL'),
#     ('SA', 'SA'),
#     ('SASU', 'SASU'),
#     ('EURL', 'EURL'),
#     ('SCI', 'SCI'),
#     ('SCOP', 'SCOP'),
#     ('SNC', 'SNC'),
#     ('GIE', 'GIE'),
# )
#     CIVILITES = (
#     ('M', 'M'),
#     ('Mme', 'Mme'),
#     ('Mlle', 'Mlle'),
#     ('Autre', 'Autre'),
# )
#     nom = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     descriptif = models.CharField(max_length=300)
#     commentaire = models.TextField() 
#     responsable_commercial = models.ForeignKey("Utilisateur", on_delete=models.SET_DEFAULT, default="Non Assigne", limit_choices_to=models.Q(responsable_commercial__fonction="Commercial"))
#     client = models.OneToOneField("Client", on_delete=models.SET_NULL, null=True)
#     def __str__(self):
#         return f"{self.descriptif} => {self.prix} $$$"