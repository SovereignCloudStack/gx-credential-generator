#!/usr/bin/env python3

"""Script to validate self-description in JSON-LD format
   against its schema is turtle format.

(c) Roman Hros <roman.hros@dnation.cloud>, 5/2023
(c) Matej Feder <matej.feder@dnation.cloud>, 5/2023
SPDX-License-Identifier: EPL-2.0
"""

from pyshacl import validate
from argparse import ArgumentParser
import rdflib

SHAPES_FILE_FORMAT = "turtle"
DATA_FILE_FORMAT = "json-ld"


def load_file(filepath, file_format=DATA_FILE_FORMAT):
    """Load file in a given format"""
    graph = rdflib.Graph()
    graph.parse(filepath, format=file_format)
    return graph


def validate_sd(sd, schema):
    """Validate SD in jsonld format against given schema in turtle format"""
    conforms, results_graph, results_text = validate(
        load_file(sd),
        shacl_graph=load_file(schema, file_format="turtle"),
        data_graph_format=DATA_FILE_FORMAT,
        shacl_graph_format=SHAPES_FILE_FORMAT,
        inference="rdfs",
        debug=False,
        serialize_report_graph=True,
    )
    print(results_text)


parser = ArgumentParser(description="Simple SD validator for development purposes")
parser.add_argument(
    "sd",
    help=f"Filepath of SelfDescription to validate. Should have {DATA_FILE_FORMAT} format",
)
parser.add_argument(
    "schema",
    help=f"Filepath of shacl schema to be used for validation. Should have {SHAPES_FILE_FORMAT} format",
)


if __name__ == "__main__":
    args = vars(parser.parse_args())
    validate_sd(**args)
