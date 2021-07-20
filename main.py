import pwnd_check
import pass_creator
import leeter

if __name__ == '__main__':
    # print('Running main')

    # password = pass_creator.make_password(12)
    # found_count = pwnd_check.check_password('password')
    leeted_pw = leeter.leet_it('password')
    # print(f'{password} found {found_count} times')
    # print(password)
    print(leeted_pw)

