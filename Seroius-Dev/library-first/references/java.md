# Java libraries

Add the dependency to `pom.xml` (Maven) or `build.gradle` (Gradle). The "Install" column shows Maven `groupId:artifactId`. Look up the newest version on Maven Central.
Check first whether the JDK already does the job: `java.time` (dates), `java.net.http.HttpClient` (HTTP), `java.nio.file` (files), streams, `record` classes, `java.util.concurrent`.

| Package | Install | Use it for |
|---|---|---|
| jackson-databind | com.fasterxml.jackson.core:jackson-databind | read and write JSON, convert objects to JSON |
| gson | com.google.code.gson:gson | simple JSON to object and back |
| guava | com.google.guava:guava | collections helpers, caching, strings, preconditions |
| commons-lang3 | org.apache.commons:commons-lang3 | string, number, object helpers, StringUtils |
| commons-csv | org.apache.commons:commons-csv | read and write CSV files |
| opencsv | com.opencsv:opencsv | read and write CSV, map rows to objects |
| poi-ooxml | org.apache.poi:poi-ooxml | read and write Excel and Word files |
| pdfbox | org.apache.pdfbox:pdfbox | read, create, edit PDF files |
| jsoup | org.jsoup:jsoup | parse HTML, scrape web pages |
| okhttp | com.squareup.okhttp3:okhttp | HTTP client, GET, POST, downloads |
| retrofit | com.squareup.retrofit2:retrofit | turn a REST API into a Java interface |
| spring-boot-starter-web | org.springframework.boot:spring-boot-starter-web | web server, REST API, full application framework |
| hibernate-core | org.hibernate.orm:hibernate-core | database ORM, map tables to classes |
| HikariCP | com.zaxxer:HikariCP | database connection pool |
| caffeine | com.github.ben-manes.caffeine:caffeine | fast in-memory cache with expiry |
| slf4j-api + logback | org.slf4j:slf4j-api and ch.qos.logback:logback-classic | logging |
| lombok | org.projectlombok:lombok | remove boilerplate: getters, setters, constructors |
| picocli | info.picocli:picocli | command-line tools, options and sub-commands |
| junit-jupiter | org.junit.jupiter:junit-jupiter | unit tests (JUnit 5) |
| mockito-core | org.mockito:mockito-core | fake objects for tests |
