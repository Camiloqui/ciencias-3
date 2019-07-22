from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Construir modelo de persona a partir del archivo person.ent
    biblioteca_model = entity_mm.model_from_file(join(this_folder, 'biblioteca.ent'))

    def is_entity(n):
        """
       
Prueba para comprobar si algún tipo es una entidad.
        """
        if n.type in biblioteca_model.entities:
            return True
        else:
            return False

    def javatype(s):
        """
        Asigna nombres de tipo de PrimitiveType a Java.
        """
        return {
                'integer': 'int',
                'string': 'String',
                'list' : 'list'
        }.get(s.name, s.name)

    # Crear carpeta de salida
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Inicializar motor de plantillas.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Filtro de registro para asignar nombres de tipo de entidad a nombres de tipo Java.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['javatype'] = javatype

    # Cargar plantilla
    template = jinja_env.get_template('python.template')

    for entity in biblioteca_model.entities:
        # Para cada entidad generar un archivo java.
        with open(join(srcgen_folder,
                       "%s.py" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

	#Cargar plantilla
   template = jinja_env.get_template('c++.template')

    for entity in biblioteca_model.entities:
        # Para cada entidad generar un archivo java.
        with open(join(srcgen_folder,
                       "%s.cpp" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

if __name__ == "__main__":
    main()
