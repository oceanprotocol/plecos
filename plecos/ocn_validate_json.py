"""Ocean Protocol wrapper around json schema"""

import click
import jsonschema as jsonschema
# @click.command()
# @click.argument('location')
# @click.option(
#     '--api-key', '-a',
#     help='your API key for the OpenWeatherMap API',
# )

@click.command()
# @click.option('--source', default="source", help='The schema version filename, must exist in /schemas folder')
# @click.argument('schema', default="metadata_v190118.json")#, help='The schema version filename, must exist in /schemas folder')
@click.argument('schema_file_name')
# @click.argument('json_file', default="metadata_v190118.json")#, help='The schema version filename, must exist in /schemas folder')
@click.argument('json_file')
# @click.option('--file', default="metadata_v190118.json", help='The schema version filename, must exist in /schemas folder')
def validate():
    """This script validates a json file according a schema file.
    Wraps the jsonschema project, see https://pypi.org/project/jsonschema/.

    Arguments:
        schema_file_name: the name of the schema file, found in ./schemas
        json_file: the relative (to current directory) path of the json file to validate against
    """
    click.echo('Hello World!')

if __name__ == "__main__":
    validate()