import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
    else:
        return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def check_password(pw_to_check):
    pw_hash = hash_it(pw_to_check)  # [0] = first 5  [1] = last of hash
    response = request_api_data(pw_hash[0])
    count = get_password_leaks_count(response, pw_hash[1])
    return count


def hash_it(pw_to_hash):
    '''
    Enter in str you want to hash w/ SHA1
    Returns hash as tuple with first 5 of hash and second half
    '''
    sha1password = hashlib.sha1(pw_to_hash.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    return first5_char, tail



if __name__ == "__main__":
    print('run main.py')