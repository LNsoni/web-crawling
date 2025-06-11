import asyncio
from typing import List, Dict
from crawl4ai import *
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
    ContentTypeFilter
)

class DeepCrawler:
    def __init__(self, verbose=False):
        self.verbose = verbose

    async def deep_crawl(self, url: str, allowed_domains: List[str], patterns: List[str], max_depth: int, max_pages: int) -> List[Dict]:
        filter_chain = FilterChain([
            DomainFilter(allowed_domains=allowed_domains),
            ContentTypeFilter(allowed_types=["text/html"]),
            URLPatternFilter(patterns=patterns)
        ])

        exclude_tags = ['footer']

        deep_crawl_strategy = BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            filter_chain=filter_chain,
            include_external=False
        )

        async with AsyncWebCrawler() as crawler:
            results: List[CrawlResult] = await crawler.arun(
                url=url,
                config=CrawlerRunConfig(
                    deep_crawl_strategy=deep_crawl_strategy,
                    scan_full_page=True,
                    exclude_external_images=True,
                    excluded_tags=exclude_tags,
                    stream=False
                ),
                bypass_cache=True
            )

            results_list = []
            seen_urls = set()

            for result in results:
                if result.url in seen_urls:
                    continue
                seen_urls.add(result.url)
                
                row = {
                    "url": result.url,
                    "media": result.media,
                    "links": result.links,
                    "markdown": result.markdown,
                    "metadata": result.metadata,
                    "status_code": result.status_code
                }
                results_list.append(row)

            return results_list

    def crawl(self, url: str, allowed_domains: List[str], patterns: List[str], max_depth: int, max_pages: int):
        return asyncio.run(self.deep_crawl(url, allowed_domains, patterns, max_depth, max_pages))
