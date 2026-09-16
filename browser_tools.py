import re
from html import unescape
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

from crewai.tools import tool


def _fetch_url(url: str) -> str:
    """Fetch a webpage and return its HTML."""

    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/120 Safari/537.36"
            )
        },
    )

    with urlopen(request, timeout=15) as response:
        return response.read().decode(
            "utf-8",
            errors="ignore"
        )


def _clean_html(html: str) -> str:
    """Convert HTML into readable plain text."""

    html = re.sub(
        r"<(script|style|noscript).*?</\1>",
        " ",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    html = re.sub(
        r"<[^>]+>",
        " ",
        html,
    )

    html = unescape(html)

    html = re.sub(
        r"\s+",
        " ",
        html,
    )

    return html.strip()


class BrowserTools:

    @staticmethod
    @tool("Scrape website content")
    def scrape_and_summarize_website(website: str) -> str:
        """
        Fetch a webpage and return its readable text so the agent can
        analyze and summarize the information.
        """

        try:
            html = _fetch_url(website)
            text = _clean_html(html)

            if not text:
                return "No readable content was found on the webpage."

            # Keep the result at a reasonable size for the LLM.
            return text[:12000]

        except Exception as error:
            return f"Unable to access website: {error}"


class SearchTools:

    @staticmethod
    @tool("Search the internet")
    def search_internet(query: str) -> str:
        """
        Search the internet for current information about a travel-related query.
        """

        try:

            search_url = (
                "https://html.duckduckgo.com/html/?q="
                + quote(query)
            )

            html = _fetch_url(search_url)

            results = []

            # Extract DuckDuckGo result links and titles.
            pattern = re.compile(
                r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                re.IGNORECASE | re.DOTALL,
            )

            matches = pattern.findall(html)

            for index, (url, title) in enumerate(matches[:8], start=1):

                clean_title = _clean_html(title)
                clean_url = unescape(url)

                if clean_title and clean_url:
                    results.append(
                        f"{index}. {clean_title}\n"
                        f"URL: {clean_url}"
                    )

            if not results:
                return (
                    "No search results were found. "
                    "Try a more specific search query."
                )

            return "\n\n".join(results)

        except Exception as error:
            return f"Search failed: {error}"
