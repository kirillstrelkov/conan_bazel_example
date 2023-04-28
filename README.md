# Simple Conan and bazel example

Hello world application with conan and bazel.

## Prerequisites

Next tools should be installed:

- bazel
- conan

## Run

Multiple ways to run example

### Script

```bash
./run.sh
```

### Build with Conan

```bash
# Install dependecies and build binary
conan build . --build=missing -of generated
```

### Build manually with bazel

```bash
# Only install and build manually
conan install . --build=missing -of generated
bazel build //:hello
```

### Run application

```bash
# Run binary
./bazel-bin/hello
```

Output:

```bash
[2023-04-28 16:07:12.936] [info] Hello World!
```
