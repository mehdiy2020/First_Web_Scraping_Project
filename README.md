# First_Web_Scraping_Project
Basic Web Scraping Project Applying Python

### The 4 arguments you should almost always use with `requests.get()`:

""""
requests.get(
    url,
    params=,     # only when URL has ? in browser
    headers=,    # ALMOST ALWAYS needed in 2025
    timeout=,    # prevents hanging forever
    cookies=     # rarely, only if logged in
)
"""

#### Use one of the following for `header=`:Prevents 403 Forbidden, makes you look like a real browser

"""
# 1. Short & works everywhere
headers = {'User-Agent': 'Mozilla/5.0'}

# 2. Current Chrome on Windows (most common)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

# 3. Current Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
}

# 4. Mac Safari
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15'
}

# 4. Microsoft Edge
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
"""


### How do we discover the correct params for any website?

There is only one correct way — look at the real browser traffic:

- Open the page in Chrome
- Press F12 → Network tab
- Do the action (search, click page 2, filter, etc.)
- Look for the request → click it → look at:
  - Request URL → copy everything after ? → those are your parameters
  - Query String Parameters tab → beautiful table of key/value


That’s it. No guessing. No standard. Each website makes up its own names.
Real examples from websites you know

#### Now you know:

- params is not always needed
- headers and timeout are almost always needed
- Every website has its own custom parameters — you discover them with F12 → Network

| Parser name       | How to use                             | Speed     | Lenient? (fixes bad HTML) | Install needed?       | Best for                 |
| ----------------- | -------------------------------------- | --------- | ------------------------- | --------------------- | ------------------------ |
| """html.parser""" | "BeautifulSoup(text, ""html.parser"")" | Medium    | Yes                       | Built-in (no install) | Beginners / always works |
| """lxml"""        | "BeautifulSoup(text, ""lxml"")"        | Very Fast | Yes                       | pip install lxml      | 99 % of real projects    |
| """html5lib"""    | "BeautifulSoup(text, ""html5lib"")"    | Very Slow | Extremely lenient,        | pip install html5lib  | Super broken HTML        |
| """xml"""         | "BeautifulSoup(text, ""xml"")"         | Fast      | No (strict)               | Built-in              | Only for XML files       |

### Here is the complete, practical cheat-sheet of BeautifulSoup’s most important methods in 2025 (the ones real scrapers use every day).

| Method                               | What it does                                | Returns                | Most common use                         |
| ------------------------------------ |---------------------------------------------|-----------------------|-----------------------------------------|
| soup.find()                          | Finds the first matching tag                | One tag object or None | "Get the first price, title, etc."      |
| soup.find_all()                      | Finds all matching tags                     | List of tag objects    | "Get all products, all links, all rows" |
| soup.select()                        | CSS selector (like `$()` in JavaScript)     | List of tag objects    | Best way for complex selectors          |
| soup.select_one()                    | CSS selector → first match only             | One tag object or None | Same as find() but with CSS power       |
| tag.get_text()                       | Gets text inside a tag                      | String                 | Extract visible text                    |             |
| tag.text                             | Same as .get_text()                         | String                 | Same                                    |
| tag['attribute']                     | "Gets attribute value (href, src, class…)"  | String or None         | "a['href']                              | img['src']" |
| tag.get('attr')                      | Safer way to get attribute                  | String or None         | tag.get('href')                         |             |
| tag.contents                         | List of children (tags + text) between tags | List                   | Loop inside a `<div>`                   |             |
| tag.parent / .parents                | Go up the HTML tree                         | One tag / generator    | Find container                          |             |
| tag.next_sibling / .previous_sibling | Move left/right in same level               | Tag or text            | Table rows                              |


+ Never use .string (it’s broken 50 % of the time)
+ Always use .get_text(strip=True) → perfect every time