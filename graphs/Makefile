# Makefile for generating and upload graphs to HDFS
# Author: Jaeho Shin <netj@cs.stanford.edu>
# Created: 2014-10-24

NUM_PARALLEL = 4
NUM_SPLITS = 100
GRAPHS = \
	 $(shell grep 'reg-bipartite:$$' Makefile | sed 's/:$$//') \
	 twitter-d-n \
	 twitter-u-n \
	 sk-2005-d-n \
	 sk-2005-u-n \
	 #

.PHONY: upload2hdfs generate
HDFS_GRAPHS_ROOT=graphs
upload2hdfs: generate
	set -eu; \
	for graph in $(GRAPHS); do \
	    ! hadoop fs -test -e $(HDFS_GRAPHS_ROOT)/$$graph || continue; \
	    hadoop fs -rmr $(HDFS_GRAPHS_ROOT)/$$graph || true; \
	    hadoop fs -mkdir $(HDFS_GRAPHS_ROOT) || true; \
	    hadoop fs -put $$graph $(HDFS_GRAPHS_ROOT)/$$graph; \
        done

generate: $(GRAPHS)

define GENERATE_K_REGULAR_BIPARTITE_GRAPH
mkdir -p $@ && export N k && \
seq $(NUM_SPLITS) | xargs -P$(NUM_PARALLEL) -L1 \
sh -xc './k-regular-bipartite-graph.py $1 $2 $(NUM_SPLITS) $$1 >$@/part-$$1' --
endef

1M-3reg-bipartite:
	$(call GENERATE_K_REGULAR_BIPARTITE_GRAPH,1000000,3)
10M-3reg-bipartite:
	$(call GENERATE_K_REGULAR_BIPARTITE_GRAPH,10000000,3)
100M-3reg-bipartite: NUM_SPLITS=500
100M-3reg-bipartite:
	$(call GENERATE_K_REGULAR_BIPARTITE_GRAPH,100000000,3)

2B-3reg-bipartite: NUM_SPLITS=5000
2B-3reg-bipartite:
	$(call GENERATE_K_REGULAR_BIPARTITE_GRAPH,2000000000,3)

# TODO random

twitter-d-n \
twitter-u-n \
sk-2005-u-n \
sk-2005-d-n:
	ln -sfnv /dfs/scratch0/iln_hadoop_backup.20140827/user/semih/gps/data/$@ .
