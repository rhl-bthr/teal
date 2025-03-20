import pickle

with open("topologies/paths/path-form/B4.json-4-paths_edge-disjoint-True_dist-metric-min-hop-dict.pkl", "rb") as f:
    paths_dict = pickle.load(f)
    for key, paths in paths_dict.items():
        print(key, paths)


with open("/home/bothra2/teal/traffic-matrices/real/B4.json_real_0_1.0_traffic-matrix.pkl", "rb") as f:
    tm = pickle.load(f).astype('int32')
    print(tm)