import re

def extract_hash(line):
    """
    Extract SHA256 hash from a Wazuh alert line.
    Returns the hash if found, otherwise None.
    """
    match = re.search(r"SHA256=([A-Fa-f0-9]{64})", line)
    if match:
        return match.group(1)
    return None


if __name__ == "__main__":
    sample = 'Hashes=MD5=123,SHA256=7C4C7725E266F12ABA8C50FD1598D4001201BCA0E7ACA901508307E365AFFF42'
    print(extract_hash(sample))
