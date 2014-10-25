#!/usr/bin/env python
# k-complete bipartite graph generator
# Author: Jaeho Shin <netj@cs.stanford.edu>
# Created: 2014-10-01

import sys
N = int(sys.argv[1] if len(sys.argv) > 1 else 10)
k = int(sys.argv[2] if len(sys.argv) > 2 else 2)
numSplits = int(sys.argv[3] if len(sys.argv) > 3 else 1)
split     = int(sys.argv[4] if len(sys.argv) > 4 else 0)

if k % 2 == 0:
    def neighbors(i):
        return (i + 2*j for j in xrange(-k/2 + 1, k/2 + 1))
else:
    def neighbors(i):
        return (i + 2*j for j in (xrange(-k/2 + 1, k/2 + 1) if i % 2 == 0
                             else xrange(-k/2 + 2, k/2 + 2)))

lb = (N/numSplits) * split     if 0 <= split and split   < numSplits else N
ub = (N/numSplits) * (split+1) if 0 <= split and split+1 < numSplits else N
for i in xrange(lb, ub):
    print "[%d, null, [%s]]" % (i+1, ",".join(str(j)
        for j in neighbors(i) if 1<=j<=N))

