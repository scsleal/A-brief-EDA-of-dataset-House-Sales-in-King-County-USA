from contextlib import contextmanager

@contextmanager
def hide_traceback() -> None:

    def is_running_from_ipython() -> bool:
        """ Checks whether running in IPython interactive console or not """
        try:
            import IPython
        except ImportError:
            return False
        try:
            from IPython import get_ipython
        except ImportError:
            return False
        else:
            return get_ipython() is not None

    # noinspection PyBroadException
    try:
        yield
    except Exception:
        if is_running_from_ipython():
            import IPython
            IPython.core.getipython.get_ipython().showtraceback(exception_only=True)
        else:
            etype, value, tb = sys.exc_info()
            print(f"{etype.__name__}: {value}")
            
            
with hide_traceback():
    1/0