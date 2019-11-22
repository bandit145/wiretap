#!/usr/bin/env python
import wiretap.wiretap as wiretap
import argparse

parser = argparse.ArgumentParser(description='wiretap bot')
parser.add_argument('-c','--config', help='config file path', required=True)
args = parser.parse_args()

def main():
	wiretap.start_bot(config=args.config)

if __name__ == '__main__':
	main()