"""Ocean Protocol wrapper around json schema"""

import click
from pathlib import Path
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
@click.argument('schema_file', type=click.Path(exists=True))
# @click.argument('json_file', default="metadata_v190118.json")#, help='The schema version filename, must exist in /schemas folder')
@click.argument('json_file', type=click.Path(exists=True))
# @click.option('--file', default="metadata_v190118.json", help='The schema version filename, must exist in /schemas folder')
def validate(schema_file, json_file):
    """This script validates a json file according a schema file.
    Wraps the jsonschema project, see https://pypi.org/project/jsonschema/.

    Arguments:

        SCHEMA_FILE_NAME: the name of the schema file, found in ./schemas

        JSON_FILE: the relative (to current directory) path of the json file to validate against
    """

    click.echo("schema_file_name: {}".format(schema_file))
    click.echo("json_file {}".format(json_file))
    print(type(schema_file))
    json_file_path = Path.cwd() / json_file
    # assert json_file_path.exists(), "Json file path {} does not exist".format(json_file_path)
    schema_file_path = Path.cwd() / schema_file
    # assert schema_file_path.exists()

    




if __name__ == "__main__":
    validate()