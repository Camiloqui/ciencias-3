from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export


this_folder = dirname(__file__)


class SimpleType(object):
    """

Estamos registrando usuario clase SimpleType para apoyar
    Tipos simples (entero, cadena) en nuestros modelos de entidad
    Por lo tanto, el usuario no necesita proporcionar enteros y cadenas
    tipos en el modelo pero pueden hacer referencia a ellos en tipos de atributos sin embargo.
    """
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name


def get_entity_mm(debug=False):
    """
   Construye y devuelve un metamodelo para el lenguaje de la entidad.
    """
    # Built-in simple types
    # Each model will have this simple types during reference resolving but
    # these will not be a part of `types` list of EntityModel.
    type_builtins = {
            'integer': SimpleType(None, 'integer'),
            'string': SimpleType(None, 'string'),
            'list': SimpleType(None, 'list')
    }
    entity_mm = metamodel_from_file(join(this_folder, 'entity.tx'),
                                    classes=[SimpleType],
                                    builtins=type_builtins,
                                    debug=debug)

    return entity_mm


def main(debug=False):

    entity_mm = get_entity_mm(debug)

    # Export to .dot file for visualization
    dot_folder = join(this_folder, 'dotexport')
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)
    metamodel_export(entity_mm, join(dot_folder, 'entity_meta.dot'))

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'biblioteca.ent'))

    # Export to .dot file for visualization
    model_export(person_model, join(dot_folder, 'biblioteca.dot'))


if __name__ == "__main__":
    main()
