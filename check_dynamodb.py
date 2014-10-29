#!/usr/bin/env python
import boto.dynamodb
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='DynaamoDB Table Nagios Check')
    parser.add_argument('-r', action='store', required=True, help='region')
    parser.add_argument('-t', action='store', required=True, help='table name')
    parser.add_argument('-w', action='store', required=True, help='warn threshold for size in MB')
    parser.add_argument('-c', action='store', required=True, help='crit threshold for size in MB')
    return parser.parse_args()

args = parse_args()
c = boto.dynamodb.connect_to_region(args.r)

def get_table_metrics(table):
    d_table = c.get_table(table)
    size = str(float(d_table.size_bytes) / 1000000)
    items = d_table.item_count
    return table, size, items


def check_thresholds(metrics):
    if float(metrics[1]) > float(args.c):
        return (2, 'CRITICAL: %s, size %s MB, Item count %s' % (metrics[0], metrics[1], metrics[2]))

    if float(metrics[1]) > float(args.w):
         return (1, 'WARNING: %s, size %s MB, Item count %s' % (metrics[0], metrics[1], metrics[2]))
    
    return (0, 'OK: %s, size %s MB, Item count %s' % (metrics[0], metrics[1], metrics[2]))
        

def main():
    metrics = get_table_metrics(args.t)
    check = check_thresholds(metrics)
    print(check[1])
    sys.exit(check[0])
    

if __name__ == "__main__":
    main()

