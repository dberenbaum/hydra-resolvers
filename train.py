from omegaconf import DictConfig
from ruamel.yaml import YAML

def main() -> None:
    cfg = DictConfig(YAML(typ="safe").load(open("params.yaml")))
    print('max epochs are ', cfg.training.pl_hparams.max_epochs)

if __name__ == "__main__":
    main()
