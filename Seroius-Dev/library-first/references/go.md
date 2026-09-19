# Go modules

Install with `go get <module path>`. This updates `go.mod`.
Check first whether the standard library already does the job: `net/http`, `encoding/json`, `encoding/csv`, `flag`, `log/slog`, `time`, `os`, `path/filepath`, `regexp`, `testing`, `sync`, `context`, `html/template`.

| Package | Install | Use it for |
|---|---|---|
| gin | go get github.com/gin-gonic/gin | web server, REST API, routes |
| cobra | go get github.com/spf13/cobra | command-line tools, sub-commands, flags |
| viper | go get github.com/spf13/viper | read settings from files, environment variables |
| zap | go get go.uber.org/zap | fast structured logging |
| testify | go get github.com/stretchr/testify | test assertions and mocks |
| gorm | go get gorm.io/gorm | database ORM |
| uuid | go get github.com/google/uuid | make unique ids |
| gorilla websocket | go get github.com/gorilla/websocket | WebSocket server and client |
| colly | go get github.com/gocolly/colly/v2 | web scraping, crawler |
| goquery | go get github.com/PuerkitoBio/goquery | parse HTML with jQuery-style selectors |
| validator | go get github.com/go-playground/validator/v10 | validate struct fields |
| jwt | go get github.com/golang-jwt/jwt/v5 | create and check JWT login tokens |
| cron | go get github.com/robfig/cron/v3 | run jobs on a schedule |
| excelize | go get github.com/xuri/excelize/v2 | read and write Excel files |
