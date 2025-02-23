import hashlib


def sha512_of_file(file_path):
    """Calculates the SHA512 hash of a file.

    Args:
        file_path: The path to the file.

    Returns:
        The SHA512 hash of the file as a hexadecimal string.
    """
    sha512_hash = hashlib.sha512()
    try:
        with open(file_path, "rb") as file:
            # Read the file in chunks to handle large files efficiently
            while chunk := file.read(8192):
                sha512_hash.update(chunk)
    except FileNotFoundError:
        return "File not found."
    return sha512_hash.hexdigest()


if __name__ == "__main__":
    # Example usage:
    input_file_path: str = "linux-6.13.1.tar.gz"
    hash_value = sha512_of_file(input_file_path)
    print(f"The SHA512 hash of {input_file_path} is:\n {hash_value}")
