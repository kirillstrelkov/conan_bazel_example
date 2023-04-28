from conan import ConanFile
from conan.tools.google import Bazel

class BazelExampleConan(ConanFile):
    name = "bazel-example"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "BazelDeps", "BazelToolchain"
    requires = "spdlog/1.11.0"

    def build(self):
        bazel = Bazel(self)
        bazel.configure()
        bazel.build(label="//:hello")
