from config import loadConfig

def main():
    config = loadConfig('config.toml')
    print("printing config:")
    print(config)

if __name__ == "__main__":
    main()