
from pathlib import Path

class Template():

    def __init__(self, source:str, dest:str = "") -> None:
        self.source = source
        self.tokens = []
        self.dest = dest


    def add_token(self, search_val:str, replace_val:str) -> None:
        self.tokens.append({
            "search": search_val,
            "replace": replace_val,
        })


    def compile(self) -> str:
        tpl = ""
        try:
            with open(self.source, "r") as file:
                tpl = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"[Template] Couldn't load '{self.source}'")

        for token in self.tokens:
            if token['replace'] is None:
                continue

            tpl = tpl.replace(token['search'], str(token['replace']))

        return tpl

    def output(self) -> None:
        compiled = self.compile()

        f_path = Path(self.dest)
        f_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.dest, "w") as file:
            file.write(compiled)
