"""
This type stub file was generated by pyright.
"""

import abc

"""Abstract and helper bases for Future implementations."""
class Future(metaclass=abc.ABCMeta):
    """Future interface.

    This interface is based on :class:`concurrent.futures.Future`.
    """
    @abc.abstractmethod
    def cancel(self):
        ...
    
    @abc.abstractmethod
    def cancelled(self):
        ...
    
    @abc.abstractmethod
    def running(self):
        ...
    
    @abc.abstractmethod
    def done(self):
        ...
    
    @abc.abstractmethod
    def result(self, timeout=...):
        ...
    
    @abc.abstractmethod
    def exception(self, timeout=...):
        ...
    
    @abc.abstractmethod
    def add_done_callback(self, fn):
        ...
    
    @abc.abstractmethod
    def set_result(self, result):
        ...
    
    @abc.abstractmethod
    def set_exception(self, exception):
        ...
    


