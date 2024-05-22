# =============================================================================
#                               REGION: TESTE 01
# =============================================================================

post_table = {
    0: {"id": 0, "body": "The post 0"}
}

def find_post(post_id):
    return post_table.get(post_id)

post = {
    "body": "teste"
}

data = dict(post)
print(data)

last_record_id = len(post_table)
print(last_record_id)

new_post = {**data, "id": last_record_id}
print(new_post)

post_table[last_record_id] = new_post
print(post_table)

print(list(post_table.values()))

outro_post = {
    "body": "teste2"
}

data = dict(outro_post)
print(data)

last_record_id = len(post_table)
print(last_record_id)

new_post = {**data, "id": last_record_id}
print(new_post)

post_table[last_record_id] = new_post
print(post_table)

print(list(post_table.values()))



from typing import Type, Optional
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True
    model_config = SettingsConfigDict(env_prefix='TEST_')


class DevelopmentConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix='DEV_')


class ProductionConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix='PROD_')


class ConfigFactory:
    config_classes = {
        'dev': DevelopmentConfig,
        'prod': ProductionConfig,
        'test': TestConfig
    }

    @staticmethod
    @lru_cache()
    def get_config(env_state: str = None) -> BaseConfig:
        if env_state is None:
            env_state = BaseConfig().ENV_STATE or 'prod'  # Default to 'prod' if ENV_STATE is not set
        config_class: Type[BaseConfig] = ConfigFactory.config_classes.get(env_state.lower(), ProductionConfig)
        return config_class()

# Usage
config = ConfigFactory.get_config()
