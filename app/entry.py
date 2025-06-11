import argparse
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd())))
from app.simplecrawl import SimpleCrawler
from app.deepcrawl import DeepCrawler

def main():
    parser = argparse.ArgumentParser(description="webcralwer cli")
    parser.add_argument("crawler_type",choices=["simple","deep"],help="Type of crawler")
    parser.add_argument("url",help="url")
    parser.add_argument("--allowed_domains",nargs='*',help="domain allowed",default=[])
    parser.add_argument("--patterns",nargs='*',help="pattern to include",default=[])
    parser.add_argument("--max_depth",type=int,help="max depth",default=2)
    parser.add_argument("--max_pages",type=int,help="pages to crawl",default=5)

    args = parser.parse_args()

    if args.crawler_type == "simple":
        crawler = SimpleCrawler()
        result = crawler.crawl(args.url)
    elif args.crawler_type == "deep":
        crawler = DeepCrawler()
        result = crawler.crawl(args.url,args.allowed_domains,args.patterns,args.max_depth,args.max_pages)
    
    print("crawler Results")
    for entry in result:
        print(entry)
    
if __name__ == " __main__":
    main()