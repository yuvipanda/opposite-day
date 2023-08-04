import sys
import ctypes

def it_is_opposite_day_now():
    """
    What is True, shall be False.

    What is False, well...
    """
    caller_frame = sys._getframe(1)
    for local_var in caller_frame.f_locals:
        
        if caller_frame.f_locals[local_var] in (True, False):
            caller_frame.f_locals[local_var] = not caller_frame.f_locals[local_var]
            # https://pydev.blogspot.com/2014/02/changing-locals-of-frame-frameflocals.html
            # This needs to be right here, and nowhere else, really.
            ctypes.pythonapi.PyFrame_LocalsToFast(
                ctypes.py_object(caller_frame),
                ctypes.c_int(0))
