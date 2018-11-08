
class Materia(object):
    
    def  __init__ ( self ):
        self.codigo =  " "
        self.nombre =  " "

    def presentar_datos(self):
        return "%s-%s-%s" % (self.obtener_codigo(), self.nombre)

    def agregar_codigo(self, n):  
        self.codigo = n

    def obtener_codigo(self):
        return self.codigo

    def agregar_nombre(self, n):  
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def presentar_datos (self):
        return "%s-%s" % (self.codigo, self.nombre)

class  MateriaPresencial (Materia):

   def __init__(self):
         
        self.num_creditos = " "

   def agregar_num_creditos(self, n):  
        self.num_creditos = n

   def obtener_num_creditos(self):
        return self.num_creditos

   def presentar_datos(self):
        return "%s-%s" % (super(MateriaPresencial, self).presentar_datos(), self.num_creditos)
