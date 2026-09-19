# C++ libraries

Install with vcpkg: `vcpkg install <name>`, or add it to `vcpkg.json` (manifest mode). Conan and system package managers (apt, brew) also work. Then use `find_package(...)` and `target_link_libraries(...)` in CMake; vcpkg prints the exact lines after install.
Check first whether the standard library already does the job: C++17/20 `<filesystem>`, `<chrono>`, `<ranges>`, `<format>` (C++20), `<optional>`, `<variant>`, `<thread>`, `<regex>`.

## Text, JSON, files, formats

| Package | Install | Use it for |
|---|---|---|
| nlohmann-json | vcpkg install nlohmann-json | read and write JSON, easy syntax |
| pugixml | vcpkg install pugixml | read and write XML, XPath |
| yaml-cpp | vcpkg install yaml-cpp | read and write YAML config files |
| tomlplusplus | vcpkg install tomlplusplus | read TOML config files |
| fmt | vcpkg install fmt | text formatting, print with placeholders |
| spdlog | vcpkg install spdlog | fast logging to console and files |
| protobuf | vcpkg install protobuf | Protocol Buffers, compact data messages between programs |
| zlib | vcpkg install zlib | compress and decompress data, gzip, zip |

## Command line, utilities

| Package | Install | Use it for |
|---|---|---|
| cli11 | vcpkg install cli11 | command-line arguments and options |
| boost | vcpkg install boost (heavy, install only needed parts, ask first) | huge toolbox: string algorithms, filesystem, program options, graphs, math |
| abseil | vcpkg install abseil | Google helper library: strings, time, containers |
| range-v3 | vcpkg install range-v3 | ranges and lazy views, functional style |
| tbb | vcpkg install tbb | parallel loops and tasks, threading building blocks |

## Networking and web

| Package | Install | Use it for |
|---|---|---|
| curl | vcpkg install curl | HTTP and FTP downloads and uploads (libcurl) |
| cpr | vcpkg install cpr | easy HTTP requests, simple wrapper over libcurl |
| cpp-httplib | vcpkg install cpp-httplib | tiny HTTP server and client, single header |
| asio | vcpkg install asio | async network sockets, timers, TCP UDP |

## Math, graphics, games, UI

| Package | Install | Use it for |
|---|---|---|
| eigen3 | vcpkg install eigen3 | matrices, vectors, linear algebra |
| glm | vcpkg install glm | graphics math, vectors, matrices for OpenGL |
| opencv | vcpkg install opencv (heavy, ask first) | computer vision, images, camera, video |
| sdl2 | vcpkg install sdl2 | window, input, audio, 2D games |
| glfw3 | vcpkg install glfw3 | OpenGL window and input |
| imgui | vcpkg install imgui | quick tool UIs, debug windows (Dear ImGui) |
| qtbase | vcpkg install qtbase (heavy, check license, ask first) | desktop app UI, Qt widgets |
| ffmpeg | vcpkg install ffmpeg (heavy, ask first) | decode, encode, convert video and audio |

## Database, security, testing

| Package | Install | Use it for |
|---|---|---|
| sqlite3 | vcpkg install sqlite3 | small embedded SQL database |
| openssl | vcpkg install openssl | TLS, HTTPS, hashes, encryption |
| libsodium | vcpkg install libsodium | modern safe encryption, hashing, keys |
| cryptopp | vcpkg install cryptopp | encryption, hashing, Crypto++ |
| gtest | vcpkg install gtest | unit tests (GoogleTest) |
| catch2 | vcpkg install catch2 | unit tests, easy syntax |
| benchmark | vcpkg install benchmark | measure code speed (Google Benchmark) |
