import os

def main():
    secret_key_1 = os.getenv('SECRET_KEY_1')
    secret_key_2 = os.getenv('SECRET_KEY_2')
    secret_key_3 = os.getenv('SECRET_KEY_3')
    print("The Keys")
    print(f"{secret_key_1 = }")
    print(f"{secret_key_2 = }")
    print(f"{secret_key_3 = }")

    print(f'Secret Key 1: {secret_key_1}')
    print(f'Secret Key 2: {secret_key_2}')
    print(f'Secret Key 2: {secret_key_3}')

if __name__ == "__main__":
    main()
