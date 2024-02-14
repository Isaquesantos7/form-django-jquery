from django.db import models

class UF(models.Model):
    index = models.BigAutoField(primary_key=True)
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=255)

    def __str__(self):

        return self.sigla
    
    class Meta:

        db_table = 'tb_uf'
        managed = True

class Municipio(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    uf = models.ForeignKey(UF, on_delete=models.PROTECT)

    def __str__(self):

        return self.nome
    
    class Meta:

        db_table = 'tb_municipio'
        managed = True

class Bairro(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):

        return self.nome
    
    class Meta:

        db_table = 'tb_bairro'
        managed = True