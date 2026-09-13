import hashlib


def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""

    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()

if __name__ == "__main__":
    file_path = "test_data/sample.txt"

    file_hash = calculate_sha256(file_path)

    print("File:", file_path)
    print("SHA-256:", file_hash)    