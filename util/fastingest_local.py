#!/usr/bin/python

import sys
import os
try:
    import json
except ImportError:
    import simplejson as json

sys.path.insert(0, "../API")
import fp

import fastingest

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print >>sys.stderr, "Usage: %s filename [-b] [json dump] ..." % sys.argv[0]
        print >>sys.stderr, "       -b: write a file to disk for bigeval"
        sys.exit(1)
    
    write_bigeval = False
    pos = 1
    
    filename = sys.argv[pos]
    pos += 1

    if sys.argv[pos] == "-b":
        write_bigeval = True
        pos += 1

    #fp.local_load(filename)
    
    for (i, f) in enumerate(sys.argv[pos:]):
        print "%d/%d %s" % (i+1, len(sys.argv)-pos, f)
        codes, bigeval = fastingest.parse_json_dump(f)
        fp.ingest(codes, do_commit=False, local=True)
        if write_bigeval:
            bename = "bigeval.json"
            if not os.path.exists(bename):
                be = {}
            else:
                be = json.load(open(bename))
            be.update(bigeval)
            json.dump(be, open(bename, "w"))
    fp.local_save(filename)
