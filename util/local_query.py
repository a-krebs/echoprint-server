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
        print >>sys.stderr, "Usage: %s local_store_filename query_code ..." % sys.argv[0]
        sys.exit(1)
    
    pos = 1
    
    filename = sys.argv[pos]
    pos += 1

    fp.local_load(filename)
    
    for (i, f) in enumerate(sys.argv[pos:]):
        #print "%d/%d %s" % (i+1, len(sys.argv)-pos, f)
        r = fp.best_match_for_query(f, local = True)
        print r.message()
        print r.TRID
