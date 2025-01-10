from json import loads, dumps
from sys import argv
from datetime import datetime


payload = loads(argv[1])


# Append package versions to be skipped.
ignore_kernel_package = {
    "6.11.11"
}



def kernel_package_selector(package):
    return (
        (package["moniker"] == "mainline" or package["moniker"] == "stable") and
        (package["version"] not in ignore_kernel_package)
    )

# Packages into a list.
payload_array = list(filter(kernel_package_selector, payload["releases"]))

# JSON would be used to create the matrix.
print(
    "array="+dumps({"include": payload_array},
    indent=None
    ),
    end=""
)


