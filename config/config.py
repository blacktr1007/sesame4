from dataclasses import InitVar, dataclass, field
from uuid import UUID


@dataclass
class SesameConfigSchema:
    uuid: InitVar[str]
    api_key: str
    secret_key: str
    device_uuid: UUID = field(init=False)

    def __post_init__(self, uuid: str):
        self.device_uuid = UUID(uuid)


@dataclass(frozen=True)
class SlackConfigSchema:
    signing_secret: str


@dataclass(frozen=True)
class GCPConfigSchema:
    project_id: str
    topic: str


@dataclass(frozen=True)
class ConfigSchema:
    history_tag: str
    sesame: SesameConfigSchema
    slack: SlackConfigSchema
    gcp: GCPConfigSchema
