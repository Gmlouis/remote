from importlib.metadata import requires, PackageNotFoundError
import platform

def min_python_version():
    min_version = tuple(map(int, platform.python_version_tuple()))
    try:
        dependencies = requires("remote")
    except PackageNotFoundError:
        print("Package not found.")
        return min_version

    if dependencies is None:
        print("No dependencies found.")
        return min_version

    for dep in dependencies:
        if 'python' in dep:
            version = tuple(map(int, dep.split('>=')[1].split('.')))
            if version > min_version:
                min_version = version
    return min_version

print(f"Minimum Python version required: {min_python_version()}")