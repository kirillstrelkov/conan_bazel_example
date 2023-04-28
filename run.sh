
rm -rf ./generated
bazel clean

# Option 1
# Install dependecies and build binary
conan build . --build=missing -of generated

# Option 2
# Only install and build manually
# conan install . --build=missing -of generated
# bazel build //:hello

# Run binary
./bazel-bin/hello