from omegaconf import OmegaConf


OmegaConf.register_new_resolver("plus_10", lambda x: x + 10)

def main() -> None:
    cfg = OmegaConf.load("params.yaml")
    print(cfg.training.pl_hparams.max_epochs)

if __name__ == "__main__":
    main()
