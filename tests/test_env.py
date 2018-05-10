import os

#to check following env variables exists or not

def testCase():
    
    env_variables=['MONGO_HOST','MONGO_PORT','CONFIG_PATH']

    for values in env_variables:

        if not os.getenv(values):
            raise AssertionError()
