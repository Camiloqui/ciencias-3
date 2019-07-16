from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from person.ent file
    biblioteca_model = entity_mm.model_from_file(join(this_folder, 'biblioteca.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in biblioteca_model.entities:
            return True
        else:
            return False

    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'int',
                'string': 'String',
                'list' : 'list'
        }.get(s.name, s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['javatype'] = javatype

    # Load template
    template = jinja_env.get_template('python.template')

    for entity in biblioteca_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%s.py" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

	#Load template
   template = jinja_env.get_template('c++.template')

    for entity in biblioteca_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%s.cpp" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

if __name__ == "__main__":
    main()
