from importlib.metadata import requires, version, PackageNotFoundError

def min_python_version():
    min_version = (0, 0)
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