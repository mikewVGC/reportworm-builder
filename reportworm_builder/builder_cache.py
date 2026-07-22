
import json
import os

class BuilderCache():

    def __init__(self, data_dir:str, prod:bool = False) -> None:
        self.meta_ssi = []
        self.data = {}

        self.data_dir = data_dir
        self.prod = prod

        os.makedirs(self.data_dir, exist_ok=True)


    def add_meta_ssi(self, file:str, title:str, description:str) -> None:
        self.meta_ssi.append({
            "file": file,
            "title": title,
            "description": description,
        })


    def add_cache_data(self, name:str, data:dict) -> None:
        self.data[name] = data


    def save(self) -> None:
        cache_data = {
            'ssi': [],
        }

        for k, d in self.data.items():
            cache_data[k] = d

        for m in self.meta_ssi:
            cache_data['ssi'].append(m)

        indent = 0 if self.prod else 2

        with open(f"{self.data_dir}/cache", 'w') as cachefile:
            cachefile.write(
                json.dumps(cache_data, indent=indent)
            )


    def load(self) -> dict:
        cache = {}
        try:
            with open(f"{self.data_dir}/cache", 'r') as cachefile:
                cache = json.loads(cachefile.read())
        except FileNotFoundError:
            print("[BuilderCache] No cache file was found")

        return cache
