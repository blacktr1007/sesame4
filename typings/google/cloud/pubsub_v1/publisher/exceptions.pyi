"""
This type stub file was generated by pyright.
"""

from google.api_core.exceptions import GoogleAPICallError

class PublishError(GoogleAPICallError):
    ...


class MessageTooLargeError(ValueError):
    """Attempt to publish a message that would exceed the server max size limit."""
    ...


class PublishToPausedOrderingKeyException(Exception):
    """Publish attempted to paused ordering key. To resume publishing, call
    the resumePublish method on the publisher Client object with this
    ordering key. Ordering keys are paused if an unrecoverable error
    occurred during publish of a batch for that key.
    """
    def __init__(self, ordering_key: str) -> None:
        ...
    


class FlowControlLimitError(Exception):
    """An action resulted in exceeding the flow control limits."""
    ...


__all__ = ("FlowControlLimitError", "MessageTooLargeError", "PublishError", "TimeoutError", "PublishToPausedOrderingKeyException")
