import setuptools
import subprocess
import os

cf_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in cf_remote_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = cf_remote_version.split("-")
    cf_remote_version = v + "+" + i + ".git." + s

assert "-" not in cf_remote_version
assert "." in cf_remote_version

assert os.path.isfile("cf_remote/version.py")
with open("cf_remote/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{cf_remote_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'spiderpen',
    version=cf_remote_version,
    author="Valentin Burillier",
    author_email="",
    description = 'Python library to control a complementary model of the LEGO Boost 17101 set',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/valentin-burillier/spiderpen',
    packages=setuptools.find_packages(),
    keywords = ['LEGO', 'ROBOTICS'],
    requires=['pylgbst'],
)
