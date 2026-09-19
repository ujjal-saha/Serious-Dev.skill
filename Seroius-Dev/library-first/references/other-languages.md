# PHP, Ruby, and other languages

For a language not listed here (Kotlin, Swift, Dart, R, Lua, and so on), use the same method: check the standard library, then search the language's official package registry, then check fit and safety as described in SKILL.md.

## PHP (Composer)

Install with `composer require <name>`. This updates `composer.json`.

| Package | Install | Use it for |
|---|---|---|
| guzzle | composer require guzzlehttp/guzzle | HTTP client, GET, POST, downloads |
| monolog | composer require monolog/monolog | logging |
| carbon | composer require nesbot/carbon | easy dates and times |
| phpdotenv | composer require vlucas/phpdotenv | load settings from a .env file |
| league csv | composer require league/csv | read and write CSV files |
| phpspreadsheet | composer require phpoffice/phpspreadsheet | read and write Excel files |
| phpunit | composer require --dev phpunit/phpunit | unit tests |

## Ruby (RubyGems)

Install with `bundle add <name>` (or `gem install <name>`). This updates the `Gemfile`.

| Package | Install | Use it for |
|---|---|---|
| nokogiri | bundle add nokogiri | parse HTML and XML, scrape pages |
| httparty | bundle add httparty | simple HTTP requests |
| rspec | bundle add rspec | unit tests |
| sidekiq | bundle add sidekiq | background jobs |
| rails | gem install rails | full web application framework |
