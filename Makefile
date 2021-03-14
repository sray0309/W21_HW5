test:
	number=1 ; while [[ $$number -le 10 ]] ; do \
        python3 hw5_tests.py && python3 hw5_tests_ec1.py && python3 hw5_tests_ec2.py ; \
        ((number = number + 1)) ; \
    done