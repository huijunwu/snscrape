#!/opt/homebrew/bin/bash -ex

export PYTHONPATH=$PYTHONPATH:./snscrape

# python3 snscrape/_cli.py --jsonl-for-buggy-int-parser twitter-tweet --recurse 1645473813214142464
#2024-05-05 12:31:11.364  CRITICAL  snscrape.base  Errors: blocked (404), blocked (404), blocked (404), blocked (404)

python3 snscrape/_cli.py twitter-user federalreserve

