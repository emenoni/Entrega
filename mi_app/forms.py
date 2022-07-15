from django import forms

class Cargar_juego(forms.Form):

    #Describimos los campos que tiene que tener nuestro formulario
   
    nombre = forms.CharField()
    max_jugadores = forms.IntegerField()
    min_edad = forms.IntegerField()


class Cargar_familiar(forms.Form):

    #Describimos los campos que tiene que tener nuestro formulario
   
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()


class Cargar_auto(forms.Form):

    #Describimos los campos que tiene que tener nuestro formulario
   
    marca = forms.CharField()
    modelo = forms.CharField()
    año = forms.IntegerField()


   