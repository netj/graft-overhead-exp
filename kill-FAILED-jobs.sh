#!/usr/bin/env bash
for jobid in $(hadoop job -list | grep '^job_' | awk '{print $1}'); do
    curl -s --show-error http://ilh01.stanford.edu:50030/jobfailures.jsp?jobid=$jobid |
        grep -q FAILED || continue
    hadoop job -kill $jobid
done
