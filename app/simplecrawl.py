import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

class SimpleCrawler:
    def __init__(self,verbose=False):
        self.browser_config=BrowserConfig(verbose=verbose)
    
    async def perform_crawl(self,url: str):
        run_config = CrawlerRunConfig(
            word_count_threshold=10,
            exclude_external_links=True,
            remove_overlay_elements=True,
            process_iframes=True
        )
        results=[]
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            result= await crawler.arun(url=url,config=run_config)
            response_data= {
                "url": result.url,
                "media": result.media,
                "links": result.links,
                "markdown": result.markdown,
                "metadata": result.metadata,
                "status_code": result.status_code
            }
            results.append(response_data)
            return results
    
    def crawl(self,url:str):
        final_result = asyncio.run(self.perform_crawl(url))
        return final_result