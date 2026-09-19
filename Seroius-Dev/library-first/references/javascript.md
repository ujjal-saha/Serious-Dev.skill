# JavaScript and TypeScript packages

Install with `npm install <name>`. This saves it in `package.json`.
Check first whether the platform already does the job: `fetch`, `URL`, `URLSearchParams`, `crypto.randomUUID()`, `structuredClone`, `Intl.DateTimeFormat`, `fs/promises`, `path`, `AbortController`, and (Node 18+) the built-in test runner `node:test`.

## Web servers and HTTP

| Package | Install | Use it for |
|---|---|---|
| express | npm install express | web server, REST API, routes |
| axios | npm install axios | HTTP calls, GET, POST, download files, interceptors, retries |
| ws | npm install ws | WebSocket server and client |
| socket.io | npm install socket.io | real-time chat, live updates, WebSocket with fallback |
| jsonwebtoken | npm install jsonwebtoken | create and check JWT login tokens |
| bcrypt | npm install bcrypt | hash passwords safely |

## Scraping and browser automation

| Package | Install | Use it for |
|---|---|---|
| cheerio | npm install cheerio | parse HTML, scrape pages, jQuery-style selectors |
| puppeteer | npm install puppeteer | control Chrome, screenshots, PDF from a page, scrape JavaScript pages |
| playwright | npm install playwright | browser automation, website testing, Chrome Firefox Safari |

## Data, dates, validation

| Package | Install | Use it for |
|---|---|---|
| lodash | npm install lodash | array and object helpers, deep clone, group, debounce |
| dayjs | npm install dayjs | small date library, format and parse dates |
| date-fns | npm install date-fns | date functions, add days, differences, formatting |
| zod | npm install zod | validate data, typed schemas, TypeScript |
| uuid | npm install uuid | make unique ids |
| papaparse | npm install papaparse | parse and write CSV files |
| xlsx | npm install xlsx | read and write Excel files (SheetJS) |
| pdf-lib | npm install pdf-lib | create and edit PDF files |
| marked | npm install marked | convert Markdown to HTML |

## Command line and settings

| Package | Install | Use it for |
|---|---|---|
| commander | npm install commander | command-line tools, options, sub-commands |
| yargs | npm install yargs | parse command-line arguments |
| inquirer | npm install inquirer | ask questions in the terminal, menus, prompts |
| chalk | npm install chalk | colored terminal text |
| dotenv | npm install dotenv | load settings from a .env file |

## Database, files, utilities

| Package | Install | Use it for |
|---|---|---|
| prisma | npm install prisma @prisma/client | database ORM with types |
| mongoose | npm install mongoose | MongoDB models and queries |
| sharp | npm install sharp | fast image resize, convert, compress |

## Front end and charts

| Package | Install | Use it for |
|---|---|---|
| chart.js | npm install chart.js | simple charts in the browser |
| d3 | npm install d3 | custom data visualizations |

## Testing

| Package | Install | Use it for |
|---|---|---|
| jest | npm install --save-dev jest | unit tests |
| vitest | npm install --save-dev vitest | fast unit tests, works well with Vite |
