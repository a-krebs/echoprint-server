import sys
import os
try:
    import json
except ImportError:
    import simplejson as json

sys.path.insert(0, "../API")
import fp

def parse_json_dump(jfile):
    codes = json.load(open(jfile))

    bigeval = {}
    fullcodes = []
    for c in codes:
        if "code" not in c:
            continue
        code = c["code"]
        m = c["metadata"]
        if "track_id" in m:
            trid = m["track_id"].encode("utf-8")
        else:
            trid = fp.new_track_id()
        length = m["duration"]
        version = m["version"]
        artist = m.get("artist", None)
        title = m.get("title", None)
        release = m.get("release", None)
        decoded = fp.decode_code_string(code)
        
        bigeval[trid] = m
        
        data = {"track_id": trid,
            "fp": decoded,
            "length": length,
            "codever": "%.2f" % version
        }
        if artist: data["artist"] = artist
        if release: data["release"] = release
        if title: data["track"] = title
        fullcodes.append(data)

    return (fullcodes, bigeval)
