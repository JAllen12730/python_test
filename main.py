def in_autotests_we_trust(a, b):
    if a == b:
        print('TEST PASSED')
    else:
        print('TEST FAILED')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)


