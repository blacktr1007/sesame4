"""
This type stub file was generated by pyright.
"""

"""Helpers for :mod:`protobuf`."""
_SENTINEL = ...
_WRAPPER_TYPES = ...
def from_any_pb(pb_type, any_pb):
    """Converts an ``Any`` protobuf to the specified message type.

    Args:
        pb_type (type): the type of the message that any_pb stores an instance
            of.
        any_pb (google.protobuf.any_pb2.Any): the object to be converted.

    Returns:
        pb_type: An instance of the pb_type message.

    Raises:
        TypeError: if the message could not be converted.
    """
    ...

def check_oneof(**kwargs): # -> None:
    """Raise ValueError if more than one keyword argument is not ``None``.

    Args:
        kwargs (dict): The keyword arguments sent to the function.

    Raises:
        ValueError: If more than one entry in ``kwargs`` is not ``None``.
    """
    ...

def get_messages(module): # -> OrderedDict[Unknown, Unknown]:
    """Discovers all protobuf Message classes in a given import module.

    Args:
        module (module): A Python module; :func:`dir` will be run against this
            module to find Message subclasses.

    Returns:
        dict[str, google.protobuf.message.Message]: A dictionary with the
            Message class names as keys, and the Message subclasses themselves
            as values.
    """
    ...

def get(msg_or_dict, key, default=...): # -> Any | object:
    """Retrieve a key's value from a protobuf Message or dictionary.

    Args:
        mdg_or_dict (Union[~google.protobuf.message.Message, Mapping]): the
            object.
        key (str): The key to retrieve from the object.
        default (Any): If the key is not present on the object, and a default
            is set, returns that default instead. A type-appropriate falsy
            default is generally recommended, as protobuf messages almost
            always have default values for unset values and it is not always
            possible to tell the difference between a falsy value and an
            unset one. If no default is set then :class:`KeyError` will be
            raised if the key is not present in the object.

    Returns:
        Any: The return value from the underlying Message or dict.

    Raises:
        KeyError: If the key is not found. Note that, for unset values,
            messages and dictionaries may not have consistent behavior.
        TypeError: If ``msg_or_dict`` is not a Message or Mapping.
    """
    ...

def set(msg_or_dict, key, value): # -> None:
    """Set a key's value on a protobuf Message or dictionary.

    Args:
        msg_or_dict (Union[~google.protobuf.message.Message, Mapping]): the
            object.
        key (str): The key to set.
        value (Any): The value to set.

    Raises:
        TypeError: If ``msg_or_dict`` is not a Message or dictionary.
    """
    ...

def setdefault(msg_or_dict, key, value): # -> None:
    """Set the key on a protobuf Message or dictionary to a given value if the
    current value is falsy.

    Because protobuf Messages do not distinguish between unset values and
    falsy ones particularly well (by design), this method treats any falsy
    value (e.g. 0, empty list) as a target to be overwritten, on both Messages
    and dictionaries.

    Args:
        msg_or_dict (Union[~google.protobuf.message.Message, Mapping]): the
            object.
        key (str): The key on the object in question.
        value (Any): The value to set.

    Raises:
        TypeError: If ``msg_or_dict`` is not a Message or dictionary.
    """
    ...

def field_mask(original, modified):
    """Create a field mask by comparing two messages.

    Args:
        original (~google.protobuf.message.Message): the original message.
            If set to None, this field will be interpretted as an empty
            message.
        modified (~google.protobuf.message.Message): the modified message.
            If set to None, this field will be interpretted as an empty
            message.

    Returns:
        google.protobuf.field_mask_pb2.FieldMask: field mask that contains
        the list of field names that have different values between the two
        messages. If the messages are equivalent, then the field mask is empty.

    Raises:
        ValueError: If the ``original`` or ``modified`` are not the same type.
    """
    ...

