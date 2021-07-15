import pwnd_check
import pass_creator

if __name__ == '__main__':
    # print('Running main')

    password = pass_creator.make_password(12)
    found_count = pwnd_check.check_password(password)

    print(f'{password} found {found_count} times')

