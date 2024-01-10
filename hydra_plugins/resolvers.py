from omegaconf import OmegaConf

def plus_10(x: int) -> int:
  return x + 10

OmegaConf.register_new_resolver('plus_10', plus_10)
