# Makefile for generating and upload graphs to HDFS
# Author: Jaeho Shin <netj@cs.stanford.edu>
# Created: 2014-10-24

NUM_PARALLEL = 4
NUM_SPLITS = 100
GRAPHS = \
	 $(shell grep 'reg-bipartite:$$' Makefile | sed 's/:$$//') \
	 #

.PHONY: upload2hdfs generate
upload2hdfs: generate
	set -eu; \
	for graph in $(GRAPHS); do \
	    ! hadoop fs -test -e graphs/$$graph || continue; \
	    hadoop fs -rmr graphs/$$graph || true; \
	    hadoop fs -put $$graph graphs/$$graph; \
        done

generate: $(GRAPHS)

define GENERATE_K_REGULAR_BIPARTITE_GRAPH
mkdir -p $@ && export N k && \
seq $(NUM_SPLITS) | xargs -P$(NUM_PARALLEL) -L1 \
sh -c './k-regular-bipartite-graph.py $1 $2 $(NUM_SPLITS) $$1 >$@/part-$$1' --
endef

1M-3reg-bipartite:
	$(call GENERATE_K_REGULAR_BIPARTITE_GRAPH,1000000,3)

1B-3reg-bipartite:
	$(call GENERATE_K_REGULAR_BIPARTITE_GRAPH,1000000000,3)

# TODO random
