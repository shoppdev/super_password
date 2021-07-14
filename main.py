import pwnd_check
import pass_creator

if __name__ == '__main__':
    print('Running main')

    # found_count = pwnd_check.check_password('Puppies')
    #
    # print(found_count, ' found')

    password = pass_creator.make_password(12)

    print(password)