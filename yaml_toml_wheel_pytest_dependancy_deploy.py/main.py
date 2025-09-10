import yaml
import toml

if __name__ == "__main__":
    with open("config_toml.toml", 'r') as config_toml:
        load_toml = toml.load(config_toml)
        print(load_toml)

    with open("config_yaml.yaml", 'r') as config_yaml:
        load_yaml = yaml.safe_load(config_yaml)
        print(load_yaml)

