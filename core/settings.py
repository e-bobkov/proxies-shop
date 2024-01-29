from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    crypto_api_key: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID"),
            crypto_api_key=env.str("CRYPTO_API_KEY")
        )
    )


settings = get_settings('.env')
print(settings)
