"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as infile:
        neos_info = csv.DictReader(infile)
        for neo in neos_info:
            # neo["pdes"] = neo["pdes"]
            neo["pha"] = True if neo["pha"] == 'Y' else False
            neo["name"] = neo["name"] or None
            neo["diameter"] = float(
                neo["diameter"]) if neo["diameter"] else float('nan')

            obj = NearEarthObject(pdes=neo["pdes"],
                                  pha=neo["pha"],
                                  name=neo["name"],
                                  diameter=neo["diameter"])

            neos.append(obj)

    # TODO: Load NEO data from the given CSV file.
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    cads = []
    with open(cad_json_path, "r") as infile:
        cad_info = json.load(infile)
        cad_info = [dict(zip(cad_info["fields"], data))
                    for data in cad_info["data"]]
        for cad in cad_info:
            # cad["des"] = cad["des"]
            # cad["cd"] = cad["cd"]
            # cad["dist"] = float(cad["dist"])
            # cad["v_rel"] = float(cad["v_rel"])

            obj = CloseApproach(des=cad["des"],
                                cd=cad["cd"],
                                dist=float(cad["dist"]),
                                v_rel=float(cad["v_rel"]))

            cads.append(obj)

    return cads
