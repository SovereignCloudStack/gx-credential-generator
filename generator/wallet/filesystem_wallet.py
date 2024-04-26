import json

from generator.wallet.wallet import Wallet
from rdflib import Graph
import os
from rdflib.exceptions import ParserError
from rdflib.plugin import PluginException

from typing import List

import glob

class FileSystemWallet(Wallet):

    def __init__(self, folder: str):
        if not os.path.isdir(folder):
            raise FileNotFoundError("Could not init wallet. Folder '" + folder + "' does not exist.")
        self.folder = folder

    def get_credential_by_id(self, cred_id: str) -> Graph:
        for cred_file in os.listdir(self.folder):
            cred_abs_path = os.path.join(self.folder, cred_file)
            if os.path.isdir(cred_abs_path):
                continue
            try:
                g = Graph()
                g.parse(cred_abs_path)
                g.query()
                for s, p, o in g:
                    print(s, p, o)
            except ParserError as e:
                print("Could not parse '" + cred_abs_path + "'." + e.msg)
            except PluginException as e:
                print("Could not parse '" + cred_abs_path + "'." + e.msg)


    def get_credentials_of_subject(self, subject_id: str, type: str = None) -> List[dict]:
        creds = []
        for cred_file in glob.glob(os.path.join(self.folder, "credentials/*.json")):
            with open(cred_file, "r") as file:
                cred_json = json.load(file)
                try:
                    if cred_json['credentialSubject']['id'] == subject_id:
                        creds.append(cred_json)
                except KeyError as ke:
                    raise KeyError("No valid credential in file: '" + cred_file + "'. Error_: " + ke)

        return creds




    def get_graph_of_subject(self, subject_id: str, type: str = None) -> Graph:
        claims_folder = os.path.join(self.folder, "claims")
        graph = Graph()
        for claim_file in os.listdir(claims_folder):
            claim_path = os.path.join(claims_folder, claim_file)
            if os.path.isdir(claim_path):
                continue
            try:
                graph = graph + Graph().parse(claim_path)
            except ParserError as e:
                print("Could not parse '" + claim_path + "'." + e.msg)
            except PluginException as e:
                print("Could not parse '" + claim_path + "'." + e.msg)

    def get_verifiable_credential(self):
        pass

    def sign_credential(self):
        pass


    def _filter_graph_by_subject(self, graph: Graph, subject: str) -> Graph:
        """
        Return all triples linked direct or transitive to given subject.
        @param subject: subject
        @return: graph, containing all triples linked direct or via transive to given subject
        """
        g = Graph()
        for s, p, o in graph:
            if s == subject:
                # geht das auch mit einer Sparql Anfrage
                pass





