from omegaconf import DictConfig
import hydra


@hydra.main(version_base=None, config_path='conf', config_name='config')
def main(cfg: DictConfig) -> None:
    print(cfg.training.pl_hparams.max_epochs)

if __name__ == "__main__":
    main()
