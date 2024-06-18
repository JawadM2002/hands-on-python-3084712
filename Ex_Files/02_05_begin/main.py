import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT) # depends on what the information is

if current_env == DEVELOPMENT: # various way of checking things
    print("Development environment") # if you change the export on terminal, it will print the expected statement
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")
