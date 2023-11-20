
import sys
import yaml
import random


def load_config(config_name):
    with open(f'{config_name}.yaml', mode = 'r', encoding = 'utf-8') as config_file:
        config = yaml.safe_load(config_file)
    

def xor():
    config = load_config()
    
    if config.get('clean text') is not None:
        byte_text = config['clean text'].encode()
        key = bytes([random.randint(0, 255) for _ in range(len(byte_text))])

        cypher = []
        
        for i in range(len(byte_text)):
            cypher.append(byte_text[i] ^ key[i])

        cypher = bytes(cypher)

        with open(config['key_file'], mode = 'wb') as key_file:
            key_file.write(key)
        
    print(config)
    
    


if __name__ == "__main__":
    xor()
