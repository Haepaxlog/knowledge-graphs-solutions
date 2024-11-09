import argparse
from urllib import request
import time
import threading
from concurrent.futures import ThreadPoolExecutor

dblp_studer_rdf_iri = "https://dblp.org/pid/s/RudiStuder"
dblp_schema_prefix = "https://dblp.org/rdf/schema#"
authorship_fragment = "authorOf"
authoredby_fragment = "authoredBy"

class Edge:
    def __init__(self, s, p, o):
        self.sub = s.replace("<", "").replace(">", "")
        self.pred = p.replace("<", "").replace(">", "")
        self.obj = o.replace("<", "").replace(">", "")

    def __str__(self):
        return f"{self.sub} {self.pred} {self.obj} ."

def is_single_authored_paper(paper, debug):
    time.sleep(2)

    resp = request.urlopen(f"{paper}.nt")

    is_authoredby_predicate = f"{dblp_schema_prefix}{authoredby_fragment}"

    data = [x.split(" ") for x in resp.read().decode('utf-8').split("\n") if x != ""]
    ntuples = [Edge(d[0], d[1], d[2]) for d in data]
    authors = [ntuple.obj for ntuple in ntuples if ntuple.pred == is_authoredby_predicate]
    if args.debug:
        print(paper, authors)

    if len(authors) == 1:
        if dblp_studer_rdf_iri in authors:
                return (paper, True)

    return (paper, False)

def main(args):
    response = request.urlopen(f"{dblp_studer_rdf_iri}.nt")
    data = [x.split(" ") for x in response.read().decode('utf-8').split("\n") if x != ""]
    ntuples = [Edge(d[0], d[1], d[2]) for d in data]

    is_author_predicate = f"{dblp_schema_prefix}{authorship_fragment}"
    papers = [ntuple.obj for ntuple in ntuples if ntuple.pred == is_author_predicate]
    if args.debug:
        print(papers)

    single_authored_papers = []
    with ThreadPoolExecutor(max_workers=len(papers)/2) as executor:
        futures = [executor.submit(is_single_authored_paper, paper, args.debug) for paper in papers]
        for future in futures:
            result = future.result()
            if result[1]:
                single_authored_papers.append(result[0])

    print("Single authored papers:", single_authored_papers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
