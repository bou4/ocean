from ocean.waveform import *

def abs():
    """Returns the absolute value of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The absolute value of n_number
    """
    raise NotImplementedError


def acos():
    """Returns the arc cosine of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: Returns the arc cosine of n_number
    """
    raise NotImplementedError


def add1():
    """Adds 1 to a floating-point number or integer.

    Args:
        number: Floating-point number or integer to increase by 1

    Returns:
        result: n_number plus 1
    """
    raise NotImplementedError


def asin():
    """Returns the arc sine of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The arc sine of n_number
    """
    raise NotImplementedError


def atan():
    """Returns the arc tangent of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The arc tangent of n_number
    """
    raise NotImplementedError


def cos():
    """Returns the cosine of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The cosine of n_number
    """
    raise NotImplementedError


def exp():
    """Raises e to a given power.

    Args:
        number: Power to raise e to

    Returns:
        result: The value of e raised to the power n_number
    """
    raise NotImplementedError


def int():
    """Returns the largest integer not larger than the given argument.

    Args:
        arg: A numeric value (which can be integer or floating point number)

    Returns:
        result: The value of the largest integer not larger than the value specified by n_arg
    """
    raise NotImplementedError


def lin_rg():
    """Returns a list of numbers in the linear range from n_from to n_to incremented by n_by.

    Args:
        from: Smaller number in the linear range
        to: Larger number in the linear range
        by: Increment value when stepping through the range

    Returns:
        range: List of numbers in the linear range
        nil: Returned if error
    """
    raise NotImplementedError


def log():
    """Returns the natural logarithm of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The natural logarithm of n_number
    """
    raise NotImplementedError


def log_rg():
    """Returns a list of numbers in the log10 range from n_from to n_to advanced by n_by.

    Args:
        from: Smaller number in the linear range
        to: Larger number in the linear range
        by: Increment value when stepping through the range

    Returns:
        range: List of numbers in the linear range
        nil: Returned if error
    """
    raise NotImplementedError


def max():
    """Returns the maximum of the values passed in.

    Requires a minimum of two arguments.

    Args:
        num1: First value to check
        num2: Next value to check
        [n_num3...]: Additional values to check

    Returns:
        result: The maximum of the values passed in
    """
    raise NotImplementedError


def min():
    """Returns the minimum of the values passed in.

    Requires a minimum of two arguments.

    Args:
        num1: First value to check
        num2: Next value to check
        [n_num3...]: Additional values to check

    Returns:
        result: The minimum of the values passed in
    """
    raise NotImplementedError


def mod():
    """Returns the integer remainder of dividing two integers.

    The remainder is either zero or has the sign of the dividend.

    Args:
        integer1: Dividend
        integer2: Divisor

    Returns:
        result:
            The integer remainder of the division.
            The sign is determined by the dividend.
    """
    raise NotImplementedError


def random():
    """Returns a random integer between 0 and x_number minus 1.

    Args:
        number: An integer

    Returns:
        result: Returns a random integer between 0 and x_number minus 1
    """
    raise NotImplementedError


def round():
    """Rounds a floating-point number to its closest integer value.

    Args:
        arg: Floating-point number

    Returns:
        result: The integer whose value is closest to n_arg
    """
    raise NotImplementedError


def sin():
    """Returns the sine of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The sine of n_number
    """
    raise NotImplementedError


def sqrt():
    """Returns the square root of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The square root of n_number
    """
    raise NotImplementedError


def srandom():
    """Sets the seed of the random number generator to a given number.

    Args:
        number: An integer

    Returns:
        t: This function always returns t
    """
    raise NotImplementedError


def sub1():
    """Subtracts 1 from a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: Returns n_number minus 1
    """
    raise NotImplementedError


def tan():
    """Returns the tangent of a floating-point number or integer.

    Args:
        number: Floating-point number or integer

    Returns:
        result: The tangent of n_number
    """
    raise NotImplementedError


def xor():
    """Returns the XOR value of the boolean inputs.

    Args:
        in1: The first boolean input
        in2: The second boolean input

    Returns:
        res: The resultant XOR value
    """
    raise NotImplementedError


def average():
    """Computes the average of a waveform over its entire range.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        overall:

    Returns:
        average: Returns a number representing the average value of the input waveform
        waveform_average: Returns a waveform (or family of waveforms) representing the average value if the input is a family of waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def abs_jitter():
    """Calculates the absolute jitter values in the intput waveform for the given threshold.

    The output waveform can be expressed in degrees, radians, or unit intervals (UI).
    The absolute jitter can be plotted as a function of cycle number, crossing time, or reference clock time.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            Valid values: rising and falling, respectively.
            Default crossType is rising.
        threshold: The threshold value against which the at which the input waveform intersects to calculate the absolute jitter
        x_unit:
            The unit defined for X-axis of the output waveform.
            Valid values: s (time) and cycle.
            Default: s

Cycle numbers refer to the n'th occurrence where the waveform crosses the given threshold.
        y_unit:
            The unit defined for Y-axis of the output waveform.
            Valid values: rad (radians), UI (unit intervals), and S (degrees)

Default value: rad.
        tnom:
            The nominal time period of the input waveform.
            The waveform is expected to be a periodic waveform that contains noise.
            If Tnom is nil, the abs_jitter function finds the approximate average time period of the input waveform.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing the absolute jitter value for the given threshold
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def analog2_digital():
    """Returns the digital form of the analog input, which can be a waveform, list or family of waveforms, or a string representation of expression(s).

    Args:
        wave: Input waveform
        threshold_type:
            Can take the values hilo or centre.
            If t_thresholdType is centre, it is a high state (1) unless its value is less than n_vc, in which case it is a low state (0).
            If t_thresholdType is hilo, any value less than n_vlo is a low state (0), any value greater than n_vhi is a high state (1) and the rest is treated as unknown based on the value of n_timex.
        vhi:
            High threshold value (used only when t_thresholdType is hilo).
            If you do not specify this value, it is calculated internally as:

vHigh = (topLine - bottomLine)*0.
            6 + bottomline.
        vlo:
            Low threshold value (used only when t_thresholdType is hilo).
            If you do not specify this value, it is calculated internally as: 

vLow = (topLine - bottomLine)*0.
            4 + bottomline.
        vc:
            Central threshold value (used only when t_thresholdType is centre).
            If you do not specify this value, it is calculated internally using vCenter = average(wave).
        time_x:
            The value that determines logic X.
            The timeX value is used to decide the state X.
            When threshold is hilo, the analog signal will be converted to logic X if:

analog signal value lies between vHigh and vLow
lapse time between vHigh and vLow is larger than timeX.

    Returns:
        dig_wave: A waveform (or a list of waveforms) is returned if the analog input specified was o_wave
        dig_val: A scalar value is returned if the analog input specified was o_val
        nil: Returns nil if the specified Waveform window does not exist
    """
    raise NotImplementedError


def awv_create_bus():
    """Creates a bus with the given digital signals and radix.

    Args:
        bus: Name of the digital waveform representing a bus
        wavelist: List of the digital waveforms in the bus
        radix: Radix of the bus
    """
    raise NotImplementedError


def awv_place_x_marker():
    """Places a vertical marker at a specific x-coordinate in the optionally specified subwindow of the specified window.

    Args:
        window_id: Waveform window ID
        x_loc: The x-coordinate at which to place the marker
        subwindow: Waveform subwindow ID
        label:

    Returns:
        x_loc: Returns a string of x-coordinates if the command is successful and the vertical marker info form is opened
        t: Returns this when the command is successful but the vertical marker info form is not opened
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def awv_place_y_marker():
    """Places a horizontal marker at a specific y-coordinate in the optionally specified subwindow of the specified window.

    Args:
        window_id: Waveform window ID
        y_loc: The y-coordinate at which to place the marker
        subwindow: Waveform subwindow ID
        label:

    Returns:
        y_loc: Returns a string of y-coordinates if the command is successful and the horizontal marker info form is opened
        t: Returns this when the command is successful but the horizontal marker info form is not opened
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def awv_refresh_output_plot_windows():
    """Refreshes all existing plot windows (with new simulation data, if any) attached with the session s_session.

    Args:
        session: Currently active environment variable
    """
    raise NotImplementedError


def b1f():
    """Returns the alternative stability factor in terms of the supplied parameters.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22

    Returns:
        waveform: Waveform object representing the alternative stability factor
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def bandwidth():
    """Calculates the bandwidth of a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        db: Positive number that defines the bandwidth
        type:
            Type of input filter.
            Valid values: "low", "high" or "band".

    Returns:
        value: Returns a number representing the value of the bandwidth if the input argument is a single waveform
        waveform: Returns a waveform (or family of waveforms) representing the bandwidth if the input argument is a family of waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def clip():
    """Restricts the waveform to the range defined by n_from and n_to.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: Starting value for the range on the X axis
        to: Ending value for the range on the X axis

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def clip_x():
    """Restricts the waveform to the range defined by n_from and n_to.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: Starting value for the range on the X axis
        to: Ending value for the range on the X axis

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def close_results():
    """Closes the simulation results stored in the input results directory.

    The function closes all the internal resources opened by the tool that are related to the results directory.
    It is recommended that you must call this function before deleting a results directory, moving the directory to any other location, or renaming a results directory.

    Args:
        dir_name: Name of the directory which was earlier used in the openResults function

    Returns:
        t: If the results database has been closed successfully
        nil: If the results database has not been closed successfully
    """
    raise NotImplementedError


def compare():
    """Compares the two given waveforms based on the specified values for absolute and relative tolerances.

    This function compares only the sections of the two waveforms where the X or independent axes overlap.

    Args:
        waveform1: Waveform 1
        waveform2: Waveform 2
        abstol:
            Absolute tolerance.
            Default value: 0.
            0.
        reltol:
            Relative tolerance.
            Default value: 0.
            0.

    Returns:
        comparison_waveform: Returns the difference of the two given waveforms based on the specified values of the relative and absolute tolerances
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def compression():
    """Performs an nth compression point measurement on a power waveform.

    Args:
        waveform: Waveform object representing output power (in dBm) versus input power (in dBm)
        x:
            The X coordinate value (in dBm) used to indicate the point on the output power waveform where the constant-slope power line begins.
            This point should be in the linear region of operation.
            Default value: Unless f_y is specified, defaults to the X coordinate of the first point of the o_waveform wave.
        y:
            The Y coordinate value (in dBm) used to indicate the point on the output power waveform where the constant-slope power line begins.
            This point should be in the linear region of operation.
            Default value: Unless f_x is specified, defaults to the Y coordinate of the first point of the o_waveform wave.
        compression:
            The delta (in dB) between the power waveform and the ideal gain line that marks the compression point.
            Default value: 1.
        io:
            Symbol indicating whether the measurement is to be input referred ('input) or output referred ('output).
            Default value: input.
        tan_slope: Default value: 1

    Returns:
        comp_point: Depending on the setting of s_measure, returns either input referred or output referred compression point
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def compression_v_r_i():
    """Performs an nth compression point measurement on a power waveform.

    Args:
        vport:
            Voltage across the output port.
            This argument must be a family of spectrum waveforms (1 point per harmonic) created by parametrically sweeping an input power (in dBm) of the circuit.
        harm:
            Harmonic index of the voltage wave contained in o_vport.
            When o_iport is specified, also applies to a current waveform contained in o_iport.
        iport:
            Current into the output port.
            This argument must be a family of spectrum waveforms (1 point per harmonic) created by parametrically sweeping an input power (in dBm) of the circuit.
            When specified, the output power is calculated using voltage and current.
            Default value: nil.
        rport:
            Resistance into the output port.
            When specified and o_iport is nil, the output power is calculated using voltage and resistance.
            Default value: 50.
        epoint:
            The X coordinate value (in dBm) used to indicate the point on the output power waveform where the constant-slope power line begins.
            This point should be in the linear region of operation.
            Default value: the X coordinate of the first point of the o_waveform wave.
        gcomp:
            The delta (in dB) between the power waveform and the ideal gain line that marks the compression point.
            Default value: 1.
        measure:
            Symbol indicating if measurement is to be input referred ('input) or output referred ('output).
            Default value: input.
        format: Default Value: power

    Returns:
        waveform: Returns a waveform when o_waveform1 is a family of waveforms
        number: Returns a number when o_waveform1 is a waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def compression_v_r_i_curves():
    """Constructs the waveforms associated with an nth compression measurement.

    Args:
        vport:
            Voltage across the output port.
            This argument must be a family of spectrum waveforms (1 point per harmonic) created by parametrically sweeping an input power (in dBm) of the circuit.
        harm:
            Harmonic index of the wave contained in o_vport.
            When o_iport is specified, also applies to a current waveform contained in o_iport.
        iport:
            Current into the output port.
            This argument must be a family of spectrum waveforms (1 point per harmonic) created by parametrically sweeping an input power (in dBm) of the circuit.
            When specified, the output power is calculated using voltage and current.
            Default value: nil.
        rport:
            Resistance into the output port.
            When specified and o_iport is nil, the output power is calculated using voltage and resistance.
            Default value: 50.
        epoint:
            The X coordinate value (in dBm) used to indicate the point on the output power waveform where the constant-slope power line begins.
            This point should be in the linear region of operation.
            Default value: the X coordinate of the first point of the o_waveform wave.
        gcomp:
            The delta (in dB) between the power waveform and the ideal gain line that marks the compression point.
            Default value: 1.
        format: Default Value: power

    Returns:
        waveform: Returns a family of waveforms containing the output power and tangent line
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def complex():
    """Creates a complex number of which the real part is equal to the real argument, and the imaginary part is equal to the imaginary argument.

    Args:
        real: The real part of the complex number
        imaginary: The imaginary part of the complex number

    Returns:
        complex: Returns the complex number
    """
    raise NotImplementedError


def complexp():
    """Checks if an object is a complex number.

    The suffix p is added to the name of a function to indicate that it is a predicate function.

    Args:
        value: A skill object

    Returns:
        t: Returns t when g_value is a complex number
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def conjugate():
    """Returns the conjugate of a waveform or number.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        x: Complex or imaginary number

    Returns:
        waveform: Returns the conjugate of a waveform if the input argument is a waveform
        y: Returns the result of n_x being mirrored against the real axis (X axis) if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def convolve():
    """Computes the convolution of two waveforms.

    Args:
        waveform1:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        waveform2: Additional waveform object
        from: Starting point (X-axis value) of the integration range
        to: Ending point (X-axis value) of the integration range
        type:
            Type of interpolation.
            Valid values: "linear" or "log".
        by: Increment

    Returns:
        waveform:
            Returns a waveform object representing the convolution if one of the input arguments is a waveform.
            Returns a family of waveforms if either of the input arguments is a family of waveforms.
        number: Returns a value representing the convolution if both of the input arguments are numbers
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def c_pwr_contour():
    """Constructs constant power contours for Z-Smith plotting.

    The trace of each contour correlates to reference reflection coefficients that all result in the same power level.

    Args:
        iwave: Current used to calculate power, expected to be a two-dimensional family of harmonic waveforms
        vwave: Voltage used to calculate power, expected to be a two-dimensional family of harmonic waveforms
        harm: Harmonic index of the waves contained in o_iwave and o_vwave
        iwave_load:
            Current used to calculate reflection coefficient, expected to be a two-dimensional family of harmonic waveforms.
            Default value: o_iwave.
        vwave_load:
            Voltage used to calculate reflection coefficient, expected to be a two-dimensional family of harmonic waveforms.
            Default value: o_vwave.
        max_power:
            Maximum power magnitude value for contours.
            Default value: automatic.
        min_power:
            Minimum power magnitude value for contours.
            Default value: automatic.
        num_cont:
            Total number of contours returned.
            Default value: 8.
        ref_imp:
            Reference resistance used to calculate reflection coefficients.
            Default value: 50.
        close_cont:
            Boolean indicating when to close the contours.
            When nil, largest segment of each contour is left open.
            Default value: nil.
        modifier:
            Symbol indicating the modifier function to apply to the calculated power.
            The modifier function can be any single argument OCEAN function such as db10 or dBm.
            Default value: dbm.
        ifam:
            vfam:

    Returns:
        waveform: Returns a family of waveforms (contours) for Z-Smith plotting
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def c_refl_contour():
    """o_iwave



Current used to calculate reflection coefficient magnitude, expected to be a two-dimensional family of spectrum waveforms.

    o_vwave



Voltage used to calculate reflection coefficient magnitude, expected to be a two-dimensional family of spectrum waveforms.
    x_harm



Harmonic index of the waves contained in o_iwave and o_vwave.
    ?iwaveLoad o_iwaveLoad



Current used to calculate reference reflection coefficient, expected to be a two-dimensional family of harmonic waveforms.
    Default value: o_iwave





?vwaveLoad o_vwaveLoad



Voltage used to calculate reference reflection coefficient, expected to be a two-dimensional family of spectrum waveforms.
    Default value: o_vwave





?maxRefl f_maxRefl



Maximum reflection coefficient magnitude value for contours.
    Default value: automatic





?minRefl f_minRefl



Minimum reflection coefficient magnitude value for contours.
    Default value: automatic





?numCont x_numCont



Total number of contours returned.
    Default value: 8





?refImp f_refImp



Reference resistance used to calculate reflection coefficients.
    Default value: 50





?closeCont g_closeCont



Boolean indicating when to close the contours.
    When nil, the largest segment of each contour is left open.
    Default value: nil.

    Args:
        waveform: Returns a family of waveforms (contours) for Z-Smith plotting
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def cross(waveform : LocalWaveform, cross_val, n, cross_type):
    """Computes the X-axis value at which a particular crossing of the specified edge type of the threshold value occurs.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        cross_val: Y-axis value at which the corresponding values of X are calculated
        n:
            Number that specifies which X value to return.
            If x_n equals 1, the first X value with a crossing is returned.
            If x_n equals 2, the second X value with a crossing is returned, and so on.
            If you specify a negative integer for x_n, the X values with crossings are counted from right to left (from maximum to minimum).
            If you specify x_n equals to 0, it returns all occurrences of the crossing events.
        cross_type:
            Type of the crossing.
            Valid values: 'rising, 'falling, 'either.
        multiple:
            An optional boolean argument that takes the value nil by default.
            If set to t, the value specified for the x_n argument is ignored and the function returns all occurrences of the crossing event.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: 'time, 'cycle.

    Returns:
        waveform: Returns a waveform if the input argument is a family of waveforms
        value: Returns the X-axis value of the crossing point if the input argument is a single waveform
        nil: Returns nil and an error message otherwise
    """
    return ws['cross'](waveform, cross_val, n, cross_type)


def db10():
    """Returns 10 times the log10 of the specified waveform object or number.

    This function can also be written as dB10.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def db20():
    """Returns 20 times the log10 of the specified waveform object or number.

    This function can also be written as dB20.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def dbm():
    """Returns 10 times the log10 of the specified waveform object plus 30.

    This function can also be written as dBm.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def delay():
    """Calculates the delay between a trigger event and a target event.

    Args:
        wf1: First waveform object
        value1: Value at which the crossing is significant for the first waveform object
        edge1:
            Type of the edge that must cross n_value1.
            Valid values: rising, falling, either

Default Value: either.
        nth1:
            Number that specifies which crossing is to be the trigger event.
            For example, if x_nth1 is 2, the trigger event is the second edge of the first waveform with the specified type that crosses n_value1.
            Default Value: 1.
        td1:
            Time at which to start the delay measurement.
            The simulator begins looking for the trigger event, as defined by o_waveform1, n_value1, t_edge1, and x_nth1, only after the n_td1 time is reached.
            Default Value: 0.
        wf2: Second waveform object
        value2: Value at which the crossing is significant for the second waveform
        edge2:
            Type of the edge for the second waveform.
            Valid values: rising, falling, either

Default Value: either.
        nth2:
            Number that specifies which crossing is to be the target event.
            For example, if x_nth2 is 2, the target event is the second edge of the second waveform with the specified type that crosses n_value2.
            Default Value: 1.
        td2:
            Time to start observing the target event.
            n_td2 is specified relative to the trigger event.
            This parameter cannot be specified at the same time as n_td2r0.
            The simulator begins looking for the target event, as defined by o_waveform2, n_value2, t_edge2, and x_nth2, only after the n_td2 time is reached

If you specify neither n_td2 nor n_td2r0, the simulator begins looking for the target event at t = 0.
            Note: For non- multiple, If td2 is specified,  find the cross point of wf1 at edge nth.
            Use this as  trigger point for target(wf2) and ignore wf2 before wf1 trigger event to find its cross point.
            Calculate the delay between two cross points.
            If td2 is not specified, find the cross point at edge nth1 of wf1 and cross point of edge nth2 of wf2 with target at time at t=0 and calculate the delay between two cross points.
        td2r0:
            Time to start observing the target event, relative to t = 0.
            Only applicable if both o_waveform1 and o_waveform2 are specified.
            This parameter cannot be specified at the same time with n_td2.
            The simulator begins looking for the target event, as defined by o_waveform2, n_value2, t_edge2, and x_nth2, only after the n_tdr0 time is reached.
            f you specify neither n_td2 nor n_td2r0, the simulator begins looking for the target event at t = 0.
            ?td2 and ?td2r0 take precedence over other options.
        stop: Time to stop observing the target event
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the riseTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of riseTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integer

Default value: 1.
        period1: Periodic interval for the first waveform
        period2: Periodic interval for the second waveform
        multiple:
            Finds all the cross points of wf1.
            If td2 is specified, finds cross points of target(wf2) staring at trigger event(first cross point of wf1) and ignore wf2 before wf1 trigger event.
            If td2 is not specified, finds cross points of target(wf2) at time at t=0.
            Calculate the delay between each of the cross points falling at interval of period1 and period2 of wf1 and wf2 respectively.
        x_name:
            Specifies whether you want to retrieve delay data against trigger time, target time (or another X-axis parameter for non-transient data) or cycle.
            Cycle numbers refer to the n'th occurrence of the delay event in the input waveform.
            The value in this field is ignored when you specify Number of Occurences as single.
        rest:
            Variable list of arguments passed to the delay function (as created from the Calculator UI).
            These variables also include support for multiple occurrences of the delay event.

    Returns:
        waveform: Returns a waveform representing the delay if the input argument is a family of waveforms
        value: Returns the delay value if the input argument is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def delay_measure():
    """Calculates the delay between a trigger event and a target event.

    Args:
        wf1: First waveform object
        wf2: Second waveform object
        edge1:
            Type of the edge that must cross n_value1.
            Valid values: rising, falling, either

Default Value: either.
        nth1:
            Number that specifies which crossing is to be the trigger event.
            For example, if x_nth1 is 2, the trigger event is the second edge of the first waveform with the specified type that crosses n_value1.
            Default Value: 1.
        value1:
            Threshold value at which the crossing is significant for the first waveform object.
            If this value is nil or blank, threshold is calculated internally using average(wave1).
        edge2:
            Type of the edge for the second waveform.
            Valid values: rising, falling, either

Default Value: either.
        value2:
            Threshold value at which the crossing is significant for the second waveform.
            If this value is nil or blank, threshold is calculated internally using average(wave2).
        nth2:
            Number that specifies which crossing is to be the target event.
            For example, if x_nth2 is 2, the target event is the second edge of the second waveform with the specified type that crosses n_value2.
            Default Value: 1.
    """
    raise NotImplementedError


def deriv():
    """Computes the derivative of a waveform with respect to the X axis.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform:
            Returns a waveform object representing the derivative with respect to the X axis of the input waveform.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def dft():
    """Computes the discrete Fourier transform and fast Fourier transform of the input waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: Starting value for the dft computation
        to: Ending value for the dft computation
        num: Number of timepoints
        window_name:
            Variable representing different methods for taking a dft computation.
            Valid values: Rectangular, ExtCosBell, HalfCycleSine, Hanning or Cosine2, Triangle or Triangular, Half3CycleSine or HalfCycleSine3, Hamming, Cosine4, Parzen, Half6CycleSine or HalfCycleSine6, Blackman, Kaiser, or Nuttall.
            For more information about windowName, see the information about Discrete Fourier Transform (dft) in the Virtuoso Analog Design Environment L User Guide.
        param1:
            Smoothing parameter.
            Applies only if the t_windowName argument is set to Kaiser.
        adc_span:
            Specifies the peak saturation level of the FFT waveform.
            When specified the magnitude of the input waveform is divided by adc span value before computing FFT.
            This is full-scale span ignoring any DC offsets.
            Valid values : Any floating point number

Default Value : 1.
            0.

    Returns:
        waveform:
            Returns a waveform representing the magnitude of the various harmonics for the specified range of frequencies.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def dftbb():
    """Computes the discrete Fourier transform (fast Fourier transform) of a complex signal.

    Args:
        waveform1: Time domain waveform object with units of volts or amps
        waveform2: Time domain waveform object with units of volts or amps
        time_start:
            Start time for the spectral analysis interval.
            Use this parameter and f_timeEnd to exclude part of the interval.
            For example, you might set these values to discard initial transient data.
        time_end: End time for the spectral analysis interval
        num:
            The number of time domain points to use.
            The maximum frequency in the Fourier analysis is directly proportionate to x_num and inversely proportional to the difference between f_timeStart and f_timeEnd.
        window_name:
            The window to be used for applying the moving window FFT.
            Valid values: Rectangular, ExtCosBell, HalfCycleSine, Hanning, Cosine2, Triangle or Triangular, Half3CycleSine or HalfCycleSine3, Hamming, Cosine3, Cosine4, Parzen, Half6CycleSine or HalfCycleSine6, Blackman, Kaiser, or Nuttall.
            Default value: Rectangular.
        smooth:
            The Kaiser window smoothing parameter.
            If there are no requests, there is no smoothing.
            Valid values: 0 <= x_smooth <= 15

Default value: 1.
        coh_gain:
            A scaling parameter.
            A non-zero value scales the power spectral density by 1/(f_cohGain).
            Valid values: 0 <= f_cohGain <= 1.
            You can use 1 if you do not want the scaling parameter to be used.
            Default value: 1.
        spectrum_type:
            A string that can be either singleSided or doubleSided.
            When this option is single-sided, the resultant waveform is only on one side of the y axis starting from 0 to N-1.
            When it is double-sided, it is symmetric to the Y axis from -N/2 to (N/2) -1.
            Default value: SingleSided.

    Returns:
        waveform_complex: The discrete Fourier transform for baseband signals of the two waveforms returned when the command is successful
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def dnl():
    """Computes the differential non-linearity of a transient simple or parametric waveform.

    Args:
        dac_signal: Waveform for which the differential non-linearity is to be calculated
        sample:
            Waveform used to obtain the points for sampling the dacSignal.
            These are the points at which the waveform crosses the threshold while either rising or falling (defined by the crossType argument) with the delay added to them.
        point_list: List of domain values at which the sample points are obtained from the dacSignal
        interval: The sampling interval
        mode:
            The mode for calculating the threshold.
            Valid values: auto and user.
            Default value: auto.
            If set to user, an n_threshold value needs to be provided.
            If set to auto, n_threshold is calculated internally.
        threshold:
            The threshold value against which the differential non-linearity is to be calculated.
            It needs to be specified only when the mode is selected as user.
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            Valid values: rising and falling, respectively.
            Default crossType is rising.
        delay:
            The delay time after which the sampling begins.
            Valid values: Any valid time value.
            Default value: 0.
        method:
            The method to be used for calculation.
            Valid values: end (end-to-end) and fit (straight line).
            Default value: end.
        units:
            Unit for expressing the output waveform.
            Valid values: abs (absolute) and lsb (multiples of least significant bit).
            Default value: abs.
        nbsamples:
            Number of samples used for calculating the non-linearity.
            If not specified, the samples are taken against the entire data window.

    Returns:
        dnl: Returns the differential waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def duty_cycle():
    """Computes the duty cycle for a given waveform as a function of time or cycle.

    Args:
        waveform: Waveform, expression, or a family of waveforms
        threshold:
            The threshold value.
            It needs to be specified only when the mode is selected as user.
        x_name:
            The X-axis of the output waveform.
            Valid values: time and cycle.
            Default value: time.
        output_type:
            Type of output.
            Valid values: average and plot.
            If set to average, the output is an average value.
            If set to plot, the output is a waveform.
            In both the cases, the output is expressed in terms of a percentage.
            Default value: plot.
        mode:
            The mode used to calculate the threshold value.
            Valid values: auto and user.
            Default value: auto.
            If you want to specify the threshold value, set the variable to user.
            If you want Virtuoso Visualization and Analysis XL to calculate the threshold value, set the variable to auto.
            The Auto Threshold Value is calculated as the average which is integral of the waveform divided by the X range.

    Returns:
        waveform: Returns a waveform that represents duty cycle as a function of time
        average: Returns the average duty cycle value as a percentage
        nil: Returns nil if the duty cycle cannot be calculated
    """
    raise NotImplementedError


def evm_q_a_m():
    """Processes the I and Q waveform outputs from the transient simulation run to calculate the Error Vector Magnitude (EVM) for multi-mode modulations.

    The function plots the I versus Q scatterplot.
    EVM is a useful measurement to describe the overall signal amplitude and phase modulated signal quality.
    It is based on a statistical error distribution normalized from an ideal digital modulation.
    Quadrature Amplitude Modulation (QAM) is a typical modulation scheme where EVM is useful.
    The EVM is calculated by detecting the I and Q signal levels corresponding to the four possible I and Q symbol combinations and calculating the difference between the actual signal level and the ideal signal level.

    Args:
        waveform_i: The waveform for the I signal
        waveform_q: The waveform for the Q signal
        t_delay:
            The start time (a numerical value) for the first valid symbol.
            This can be obtained from the Waveform Viewer window by recording the time of the first minimum or first maximum (whichever is earlier) on the selected signal stream.
        sampling_t:
            A sampling time (a numerical value) for the symbol.
            Each period is represented by a data rate.
            The data rate at the output is determined by the particular modulation scheme being used.
        levels:
            The modulation levels.
            Valid values: 4, 16, 64, 256

Default value: 4.
        normalize:
            An option to see the scatter plot normalized to the ideal values +1 and -1 (for example, when superimposing scatter plots from different stages in the signal flow, where the levels may be quite different but you want to see relative degradation or improvement in the scatter).
            This option does not affect the calculation of the EVM number.
            Valid values: nil, t

Default value: t.
        percent:

    Returns:
        waveform: Returns a waveform object representing the EVM value computed from the input waveforms
        nil: Returns nil and an error message if the function is unsuccessful
    """
    raise NotImplementedError


def evm_qpsk():
    """Processes the I and Q waveform outputs from the transient simulation run to calculate the Error Vector Magnitude (EVM) and plot the I versus Q scatterplot.

    EVM is a useful measurement to describe the overall signal amplitude and phase modulated signal quality.
    It is based on a statistical error distribution normalized from an ideal digital modulation.
    Quadrature Phase Shift Keying (QPSK) is a typical modulation scheme where EVM is useful.
    The EVM is calculated by detecting the I and Q signal levels corresponding to the four possible I and Q symbol combinations and calculating the difference between the actual signal level and the ideal signal level.

    Args:
        waveform1: The waveform for the I signal
        waveform2: The waveform for the Q signal
        t_delay:
            The start time for the first valid symbol.
            This can be obtained from the Waveform Viewer window by recording the time of the first minimum or first maximum (whichever is earlier) on the selected signal stream.
        sampling:
            A period for the symbol.
            Each period is represented by a data rate.
            The data rate at the output is determined by the particular modulation scheme being used.
        auto_level_detect:
            An option to indicate that you want the amplitude (n_voltage) and DC offset (n_offset) to be automatically calculated.
            Amplitude is calculated by averaging the rectified voltage level of the signal streams and DC offset by averaging the sum of an equal number of positive and negative symbols in each signal stream.
            These values are used to determine the EVM value.
            If this value is set to nil, you must specify values for n_voltage and n_offset.
            Valid values: 'nil, 't

Default value: 't.
        voltage: The amplitude of the signal
        offset: The DC offset value
        normalize:
            An option to see the scatter plot normalized to the ideal values +1 and -1 (for example, when superimposing scatter plots from different stages in the signal flow, where the levels may be quite different but the you want to see relative degradation or improvement in the scatter).
            This option does not affect the calculation of the EVM number.
            Valid values: nil,t

Default value: nil.
        percent:

    Returns:
        waveform: Returns a waveform object representing the EVM value computed from input waveforms
        nil: Returns nil and an error message if the function is unsuccessful
    """
    raise NotImplementedError


def eye_diagram():
    """Returns an eye-diagram plot of the input waveform signal.

    It returns the waveform object of the eye-diagram plot.
    Using an advanced option, the function also calculates the maximum vertical and horizontal opening of the eye formed when the input waveform is folded by the specified period to form the eye.

    Args:
        waveform: Input waveform signal
        start: The X-axis start value from where the eye-diagram plot is to begin
        stop: The X-axis stop value where the eye-diagram plot is to terminate
        period: The period after which the waveform is to be folded to form the eye
        adv_options:
            Specifies whether the vertical (Max Vertical Opening) or horizontal opening (Max Horizontal Opening) of the eye is to be calculated.
            Valid values: vertical, horizontal

Default value: nil.
        intensity_plot: Boolean used to specify whether to generate a high intensity eye diagram plot

    Returns:
        waveform: Returns a waveform object representing the eye-diagram plot of the input waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def eye_height_at_x_y():
    """Calculates the eye height at the specified point (x,y) inside the eye diagram.

    Eye height is the difference of two intercepts made with the innermost traces of the eye in the y-axis direction.

    Args:
        eye_diagram: The eye diagram waveform that is used to calculate the eye height
        x: The x-axis value that is used to calculate the eye height
        y: The y-axis value that is used to calculate the eye height

    Returns:
        eye_height: Returns the eye height at the specified point (x,y) inside the eye diagram
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def eye_width_at_x_y():
    """Calculates the eye width at the specified point (x,y) inside the eye diagram.

    Eye width is the difference of two intercepts made with the innermost traces of the eye in the x-axis direction.

    Args:
        eye_diagram: The eye diagram waveform that is used to calculate the eye width
        x: The x-axis value that is used to calculate the eye width
        y: The y-axis value that is used to calculate the eye width

    Returns:
        eye_width: Returns the eye width at the specified point (x,y) inside the eye diagram
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def eye_aperture():
    """Returns the aperture of the input eye diagram signal.

    Args:
        waveform: Input signal, which is a eye diagram waveform for which aperture is to be calculated
        vref: Reference voltage
        ac_height: AC height, which specifies the height of the left side of the aperture window
        dc_height: DC height, which specifies the height of the right side of the aperture window
        plot_box:
            Specifies whether to display the aperture in the eye diagram or calculate the eye width.
            Valid values: t or nil.
            When this argument is set to t, the eye aperture is displayed in the output plot.
            When set to nil, the eye aperture width is returned.
        optimize:
            Specifies whether to calculate the reference voltage that can be used to achieve the maximum eye aperture width.
            Valid values: t or nil.

    Returns:
        waveform: Returns the output waveform with eye aperture plotted
        aperture_width: Returns the aperture width
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def eye_measurement():
    """Evaluates the measurements for the eye diagram plot.

    Args:
        waveform: The eye diagram waveform
        sample:
            The time interval after which the signals are divided in the eye diagram plot.
            If this field is left blank, the data within the level 1 and level 0 regions are used to analyze the amplitude variation of the signal.
            This means there is some sensitivity to the actual spacing between the data points in the signal, which is caused by the variable time steps in the simulator.
            If the points are clustered in the curve portion, the distribution can be skewed.
            To perform the analysis, the sampling interval you specify in this field is divided into even time points.
        auto: When this argument is set to true, then the following agument values are computed automatically:

horizThreshold, startx0, startx1, xTypePercent0, xTypePercent1, endx0, endx1, yTypePercent0, yTypePercent1, starty0, endy0, starty1, and endy1
        horiz_threshold:
            The Y-axis level (for example voltage) that represents the switching threshold of the signal, typically half the signal range.
            This is used to compute statistical information about the threshold.
        sample:
            The time interval after which the signals are divided in the eye diagram plot.
            If this field is left blank, the data within the level 1 and level 0 regions are used to analyze the amplitude variation of the signal.
            This means there is some sensitivity to the actual spacing between the data points in the signal, which is caused by the variable time steps in the simulator.
            If the points are clustered in the curve portion, the distribution can be skewed.
            To perform the analysis, the sampling interval you specify in this field is divided into even time points.
        x_type_percent0:
            Level0 X-range specified whether specified in "%".
            If the value is t, it signifies the "%" value and if the value is nil, it signifies the absolute value.
            Default value is t.
        startx0:
            Level0 X-range start value.
            Default value is 40.
        starty0:
            Level0 Y-range start value.
            Default value is 0.
        y_type_percent0:
            Level0 Y-range specified whether specified in "%".
            If the value is t, it signifies the "%" value and if the value is nil, it signifies the absolute value.
            Default value is t.
        endx0:
            Level0 X-range end value.
            Default value is 60.
        endy0:
            Level0 Y-range end value.
            Default value is 50.
        x_type_percent1:
            Level1 X-range specified whether specified in "%".
            If the value is t, it signifies the "%" value and if the value is nil, it signifies the absolute value.
            Default value is t.
        startx1:
            Level1 X-range start value.
            Default value is 40.
        starty1:
            Level1 Y-range start value.
            Default value is 50.
        y_type_percent1:
            Level1 Y-range specified whether specified in "%".
            If the value is t, it signifies the "%" value and if the value is nil, it signifies the absolute value.
            Default value is t.
        endx1:
            Level1 X-range end value.
            Default value is 60.
        endy1:
            Level1 Y-range end value.
            Default value is 100.
        no_of_bins:
            Number of signal bins to be displayed in the eye diagram plot.
            These signals bins are used to form the horizontal (threshold crossing times) and vertical (amplitude variation) histograms.
        measure:
            Computes one of the measurement values described below:


level0Mean (Level0 Mean)—Mean of the Y-values within the level0 region.
            level0Stddev (Level0 Stddev)—Standard deviation of the Y-values within the level0 region.
            level1Mean (Level1 Mean)—Mean of the Y-values within the level1 region.
            level1Stddev (Level1 Stddev)—Standard deviation of the Y-values within the level1 region.
            amplitude (Eye amplitude)—Mean to mean amplitude of the eye, computed as: Meanlevel1 - Meanlevel0.
            height (Eye height)—Vertical opening of the eye, computed as:
(Meanlevel1 - 3*level1) - (Meanlevel0 - 3*level0).
            signalToNoise (Eye signalToNoise)—Signal to noise ratio of the eye, computed as:
(Meanlevel1 - Meanlevel0) / (level1 + level0).
            thresholdCrossingStddev (Threshold crossing stddev)—Threshold crossing standard deviation is computed only when there is a single transition region in the eye diagram because it is analyzed over the entire period.
            thresholdCrossingAverage (Threshold crossing average)—This is computed over the entire period.
            width (Eye width)—Represents the opening of the eye in the X direction.
            It is computed as:
(Meantransition2 - 3*std(transition2)) - (Meantransition1 - 3*std(transition1)).
        ():
            riseTime (Eye Rise Time)—Two thresholds taken at the 20% and 80% points between the level0 mean and level1 mean.
            At each of these two thresholds, a horizontal histogram is computed, which is an analysis of the crossing points of these two thresholds, and the resulting rise time is the difference in the mean crossing point at each of these two thresholds.
            fallTime (Eye Fall Time)—Signal measured between the percent high and percent low of the difference between the initial and final value.
            randJitterLeft—Random jitter calculated from the crossing histogram of the left crossing area
randJitterRight—Random jitter calculated from the crossing histogram of the right crossing area
determJitter—Average deterministic jitter of the crossing areas.

    Returns:
        waveform: Returns the computed scalar value or a waveform for the specific measure that was passed
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def edge_triggered_eye_diagram():
    """Returns a signal triggered at the beginning of the eye diagram instead of a fixed period.

    Args:
        waveform: The eye diagram waveform
        start: The X-axis start value from where the eye diagram plot is to begin
        stop: The X-axis stop value where the eye diagram plot is to terminate
        trigger_wave: The waveform that is used for triggering the eye diagram
        threshold: The Y-axis value of trigger wave at which the corresponding cross points of the trigger wave are calculated
        edge_type:
            Type of the crossing.
            Valid values: rising, falling, either.
        trigger_offset: The value by which the trigger wave should be l-shifted to align with the input waveform signal
        intensity_plot: Controls the intensity based plotting of the eye diagram

    Returns:
        waveform: Returns the computed scalar value or a waveform for the specific measure that was passed
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def flip():
    """Returns a waveform with the X vector values negated.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform:
            Returns a waveform object representing the input waveform mirrored about its Y axis.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def four_eval():
    """Evaluates the Fourier series represented by an expression.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: Starting point on the X axis at which to start the evaluation
        to: Increment
        by: Ending point on the X axis
        base_band:
            Accepts boolean values t or nil.
            The default value is nil.
            When set to t, the function evaluates the baseband version of the inverse of the dft function by converting the unsymmetrical spectrum to a symmetrical one.

    Returns:
        waveform:
            Returns a waveform object representing the inverse Fourier transformation of the input waveform.
            Returns a family of waveforms if the input argument is a family of waveforms.
            Returns the baseband version of the inverse of the dft function if baseBand is set to t.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def fall_time():
    """Returns the fall time measured between theta1 (percent high) to theta2 (percent low) of the difference between the initial value and the final value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        init_val: Initial value at which to start the computation
        init_type:
            Specifies how n_initVal functions.
            Valid values: a non-nil value specifies that the initial value is taken to be the value of the waveform, interpolated at n_initVal, and the waveform is clipped from below as follows:

o_waveform = clip( o_waveform g_initVal nil ) 

where nil specifies that n_initVal is defined by the X value entered.
            (The command gets the Y value for the specified X value and uses that value for n_initVal.
            ).
        final_val: Final value at which to end the computation
        final_type:
            Specifies how the n_finalVal argument functions.
            Valid values: a non-nil value specifies that the final value is taken to be the value of the waveform, interpolated at n_finalVal, and the waveform is clipped from above, as follows:

o_waveform = clip(o_waveform nil n_finalVal)

where nil specifies that the n_finalVal argument is defined by the X value entered.
            (The command gets the Y value for the specified X value and uses that value for n_finalVal.
            ).
        theta1: Percent high
        theta2: Percent low
        multiple:
            An optional boolean argument that takes the value nil by default.
            If set to t, the function returns multiple occurrences of the fallTime event.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: 'time, 'cycle.
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the fallTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of fallTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integerDefault value: nil.

    Returns:
        waveform: Returns a waveform representing the fall time for a family of waveforms if the input argument is a family of waveforms or if g_multiple is set to t
        value: Returns a value for the fall time if the input is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def freq():
    """Computes the frequency of the input waveform(s) as a function of time or cycle.

    Args:
        waveform: Waveform, expression, or a family of waveforms
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            For the freq function, you may specify the frequency to be calculated against either the rising points or the falling points by setting crossType to rising or falling, respectively.
            The default crossType is rising.
        threshold:
            The threshold value against which the frequency is to be calculated.
            This needs to be specified only when the mode selected is user.
        mode:
            The mode for calculating the threshold.
            This is auto, by default, in which case n_threshold is calculated internally.
            It can alternatively be set to user, in which case, an n_threshold value needs to be provided.
            Default Value: auto.
        x_name:
            The X-axis of the output waveform.
            The default value is time but cycle is also a valid value.
            Default Value: time.
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the riseTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of riseTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integer

Default value: 1.

    Returns:
        output_wave: Returns the frequency as a function of time or cycle
        nil: Returns nil if the frequency cannot be calculated
    """
    raise NotImplementedError


def freq_jitter():
    """Calculates the frequency jitter.

    Args:
        waveform: Waveform, expression, or a family of waveforms
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            Valid values: rising and falling.
            Default value: rising.
        mode:
            The mode for calculating the threshold.
            Valid values: auto and user.
            If set to user, an n_threshold value needs to be provided.
            If set to auto, n_threshold is calculated internally.
            Default value: auto.
        threshold:
            The threshold value against which the frequency is to be calculated.
            It needs to be specified only when the mode selected is user.
        bin_size:
            The width of the moving average window.
            The deviation of value at the particular point from the average of this window is the jitter.
            Default value: 0.
        x_name:
            The X-axis of the output waveform.
            Valid values: time and cycle.
            Default value: time.
        output_type:
            Type of output.
            Valid values: sd and plot.
            If set to sd, the output is a standard deviation jitter.
            If set to plot, the output is a waveform.
            Default value: plot.

    Returns:
        waveform: Returns the frequency jitter values as a function of time or cycle when the outputType is set to plot
        val: Returns the standard deviation value when the outputType is set to sd
        nil: Returns nil otherwise
    """
    raise NotImplementedError


def frequency():
    """Computes the reciprocal of the average time between two successive midpoint crossings of the rising waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns a waveform representing the frequency of a family of waveforms if the input argument is a family of waveforms
        value: Returns a number representing the frequency of the specified waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ga():
    """Returns the available gain in terms of the supplied parameters and the optional source reflection coefficient (Gs).

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        gs:
            Source reflection coefficient.
            Default value: 0.

    Returns:
        waveform: Waveform object representing the available gain
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gac():
    """Computes the available gain circles.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        level:
            Level in dB.
            It can be specified as a scalar or a vector.
            If it is specified as a vector, the level is swept.
            The linRg function can be called to generate a linear range.
            For example, linRg( -30 30 5 ) is the same as list(-30 -25 -20 -15 -10 -5 0 5 10 15 20 25 30) and the g_level argument can be specified as either of the above.
            In that case, an available gain circle is calculated at each one of the 13 levels.
        frequency:
            Frequency, which can be specified as a scalar or a linear range.
            If it is specified as a linear range, the frequency is swept.
            The linear range is specified as a list with three values: the start of the range, the end of the range, and the increment.
            For example, list(100M 1G 100M) specifies a linear range with the following values:

{ 100M, 200M, 300M, 400M, 500M, 600M, 700M, 800M, 900M, 1G }

In that case, an available gain circle is calculated at each one of the 10 frequencies.

    Returns:
        waveform: Waveform object representing the available gain circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gain_bw_prod():
    """Calculates the gain-bandwidth product of a waveform representing the frequency response of interest over a sufficiently large frequency range.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns a waveform representing the gain-bandwidth product for a family of waveforms if the input argument is a family of waveforms
        value: Returns a value for the gain-bandwidth product for the specified waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gain_margin():
    """Computes the gain margin of the loop gain of an amplifier.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        stable: Boolean optional value that takes the value nil by default

    Returns:
        waveform: Returns a waveform representing the gain margin for a family of waveforms if the input argument is a family of waveforms
        value: Returns the value for the gain margin of the specified waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmax():
    """Returns the maximum power gain in terms of the supplied parameters.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22

    Returns:
        waveform: Load reflection coefficient
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmin():
    """Returns the optimum noise reflection coefficient in terms of o_Gopt, o_Bopt, and f_zref.

    Args:
        gopt: Waveform object representing the optimum source conductance
        bopt: Waveform object representing the optimum source susceptance
        zref: Reference impedance

    Returns:
        gmin_wave: Waveform object representing the optimum noise reflection coefficient
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmsg():
    """Returns the maximum stable power gain in terms of the supplied parameters.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22

    Returns:
        waveform: Waveform object representing the maximum stable power gain
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmux():
    """Returns the maximum unilateral power gain in terms of the supplied parameters.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22

    Returns:
        waveform: Waveform object representing the maximum unilateral power gain
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gp():
    """Computes the power gain in terms of the S-parameters.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        gl:
            Load reflection coefficient.
            Default value: 0.

    Returns:
        waveform: Waveform object representing the power gain
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gpc():
    """Computes the power gain circles.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        level:
            Level in dB.
            It can be specified as a scalar or a vector.
            If it is specified as a vector, the level is swept.
            The linRg function can be called to generate a linear range.
            For example, linRg( -30 30 5 ) is the same as list(-30 -25 -20 -15 -10 -5 0 5 10 15 20 25 30) and the g_level argument can be specified as either.
            In that case, a power gain circle is calculated at each one of the 13 levels.
        frequency:
            The frequency.
            It can be specified as a scalar or a linear range.
            If it is specified as a linear range, the frequency is swept.
            The linear range is specified as a list with three values: the start of the range, the end of the range, and the increment.
            For example, list(100M 1G 100M) specifies a linear range with the following values:

{ 100M, 200M, 300M, 400M, 500M, 600M, 700M, 800M, 900M, 1G }

In that case, a power gain circle is calculated at each one of the 10 frequencies.

    Returns:
        waveform: Waveform object representing the power gain circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def group_delay():
    """Computes the group delay of a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns a waveform representing the group delay of the specified waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gt():
    """Returns the transducer gain in terms of the supplied parameters and the optional source reflection coefficient (Gs) and the input reflection coefficient (Gl).

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        gs:
            Source reflection coefficient.
            Default value: 0.
        gl:
            Input reflection coefficient.
            Default value: 0.

    Returns:
        waveform: Waveform object representing the transducer gain
        nil: Returns nil and displays a message if there is an error
    """
    raise NotImplementedError


def harmonic():
    """Returns the waveform for a given harmonic index.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        index:
            The index number that designates the harmonic information to be returned.
            For the 'pss, 'pac, and 'pxf analyses, the index is an integer number.
            For the 'pdisto analysis, the index is a list of integers that correspond with the frequency names listed in the funds analysis parameter in the netlist.
            If more than one h_index is desired at one time, a list can be specified.

    Returns:
        waveform: Returns a waveform (when a single h_index is specified) or family of waveforms (when more than one h_index is specified) if the input argument is a family of waveforms
        value: Returns the harmonic value if the input is a single waveform with the X values being harmonics
        nil: Returns nil and displays a message if there is an error
    """
    raise NotImplementedError


def harmonic_freq_list():
    """Returns a list of lists, with each sublist containing a harmonic index and the minimum and maximum frequency values that the particular harmonic ranges between.

    Args:
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
        s_result_name: Results from an analysis

    Returns:
        list:
            Returns a list of lists.
            For the 'pss, 'pac, and 'pxf analyses, the first element of each sublist is an integer number.
            For the 'pdisto analysis, the first element of each sublist is a list of integers that correspond with the frequency names listed in the funds analysis parameter in the netlist.
            For all sublists, the remaining entries are the minimum and maximum frequency values that the particular harmonic ranges between.
            If both of these frequency values are the same, just one frequency value is returned.
        nil: Returns nil if no harmonics are found in the data
    """
    raise NotImplementedError


def harmonic_list():
    """Returns the list of harmonic indices available in the resultName or current result data.

    Args:
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
        s_result_name: Results from an analysis

    Returns:
        list:
            Returns a list of harmonic indices.
            For the 'pss, 'pac, and 'pxf analyses, the index is an integer number.
            For the 'pdisto analysis, the index is a list of integers that correspond with the frequency names listed in the 'funds analysis parameter in the netlist.
        nil: Returns nil if no harmonics are found in the data
    """
    raise NotImplementedError


def histo():
    """Returns a waveform that represents the statistical distribution of input data in the form of a histogram.

    The height of the bars (or bins) in the histogram represents the frequency of the occurrence of values within a specific period.
    Using the histo function, the range for capturing these frequencies can be specified through the n_min and n_max values.

    Args:
        waveform: Input waveform
        bins: Number of bins to represent the input data
        min:
            The first value on the horizontal axis of the histogram.
            By default, it assumes the minimum value of the input waveform.
        max:
            The last value on the horizontal axis of the histogram.
            By default, it assumes the maximum value of the input waveform.

    Returns:
        histo_waveform: Returns a waveform representing the statistical distribution of the input waveform o_waveform
        nil: Returns nil in case of an error
    """
    raise NotImplementedError


def histogram2_d():
    """Returns a waveform that represents the statistical distribution of input data in the form of a histogram.

    The height of the bars (or bins) in the histogram represents the frequency of the occurrence of values within a specific period.

    Args:
        waveform: Input waveform
        nbins:
            Number of bins (bars) to be plotted in the resulting histogram plot.
            Valid values: 1 to 50.
            Default value:10.
        type:
            Type of histogram to be plotted.
            Valid values: Standard, Cumulative line, and Cumulative box.
            Default value: Standard.
        set_annotation:
            Boolean specifying whether to display the standard deviation lines in the resulting histogram plot.
            Valid values: t or nil

Default value: nil.
        set_density_estimator:
            Boolean specifying whether the resulting histogram plot display a curve that estimates the distribution concentration.
            Valid values: t or nil

Default value: nil.

    Returns:
        waveform: Returns a waveform representing the statistical distribution of the input waveform o_waveform
        nil: Returns nil in case of an error
    """
    raise NotImplementedError


def iinteg():
    """Computes the indefinite integral of a waveform with respect to the X-axis variable.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns a waveform representing the indefinite integral of the input waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def imag():
    """Returns the imaginary part of a waveform representing a complex number or returns the imaginary part of a complex number.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        input: Complex number

    Returns:
        waveform_imag: Returns a waveform when the input argument is a waveform
        number_imag: Returns a number when the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def inl():
    """Computes the integral non-linearity of a transient simple or parametric waveform.

    Args:
        dac_signal: Waveform for which the integral non-linearity is to be calculated
        sample:
            Waveform used to obtain the points for sampling the dacSignal.
            These are the points at which the waveform crosses the threshold while either rising or falling (defined by the crossType argument) with the delay added to them.
        point_list: List of domain values at which the sample points are obtained from the dacSignal
        interval: The sampling interval
        mode:
            The mode for calculating the threshold.
            Valid values: auto and user.
            Default value: auto.
            If set to user, an n_threshold value needs to be provided.
            If set to auto, n_threshold is calculated internally.
        threshold:
            The threshold value against which the integral non-linearity is to be calculated.
            It needs to be specified only when the mode is selected as user.
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            Valid values: rising and falling, respectively.
            Default crossType is rising.
        delay:
            The delay time after which the sampling begins.
            Valid values: Any valid time value.
            Default value: 0.
        unit:
            Unit for expressing the output waveform.
            Valid values: abs (absolute) and lsb (multiples of least significant bit).
            Default value: abs.
        nbsamples:
            Number of samples used for calculating the non-linearity.
            If not specified, the samples are taken against the entire data window.

    Returns:
        inl: Returns the integral non-linearity waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def integ():
    """Computes the definite integral of the waveform with respect to a range specified on the X-axis of the waveform.

    The result is the value of the area under the curve over the range specified on the X-axis.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        initial_limit_n: Initial limit for definite integration
        final_limit_n: Final limit for definite integration

    Returns:
        waveform: Returns a waveform representing the definite integral for a family of waveforms if the input argument is a family of waveforms
        value: Returns a numerical value representing the definite integral of the input waveform if the input argument is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def intersect():
    """Returns a waveform containing the points of intersection for two waveforms passed as arguments.

    Args:
        waveform1:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        waveform2: Additional waveform object

    Returns:
        wave: Returns a waveform containing the points of intersection for the two waveforms passed as arguments
        nil: Returns nil if the two waveforms are disjoint or overlap each other, and an error message, if the arguments to the function are not correct
    """
    raise NotImplementedError


def ipn():
    """Performs an intermodulation nth-order intercept measurement.

    Args:
        spurious: Waveform or number representing the spurious output power (in dBm)
        reference: Waveform or number representing the reference output power (in dBm)
        ordspur:
            Order or slope of the spurious constant-slope power line.
            Default value: 3.
        ordref:
            Order or slope of the reference constant-slope power line.
            Default value: 1.
        epspur:
            Value (in dBm) used to indicate the point where the spurious constant-slope power line begins.
            If g_psweep is t, this value is the input power value of the point on the o_spurious waveform, otherwise this value is paired with the o_spurious value to define the point.
            This point should be in the linear region of operation.
            (If g_psweep is t, f_spspur defaults to the X coordinate of the first point of the o_spurious wave; if s_measure is 'input, a number must be specified.
            ).
        epref:
            Value (in dBm) used to indicate the point where the reference constant-slope power line begins.
            If g_psweep is t, this value is the input power value of the point on the o_reference waveform, otherwise this value is paired with the o_reference value to define the point.
            This point should be in the linear region of operation.
            (If g_psweep is t, f_epref defaults to the X coordinate of the first point of the o_reference wave; if s_measure is 'input, a number must be specified.
            ).
        psweep:
            Boolean indicating that the input power to the circuit was a parametric sweep.
            The power sweep must both be in dBm and be performed at the lowest parametric level.
            Default value: t.
        measure:
            Name indicating if measurement is to be input referred ('input) or output referred ('output).
            Default value: 'input.

    Returns:
        waveform: Depending on setting of g_psweep and the dimension of the input waveforms, returns either a waveform or a family of waveforms
        number: If o_spurious and o_reference are numbers or they are waveforms when g_psweep is t, returns a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ipn_v_r_i():
    """Performs an intermodulation nth-order intercept point measurement.

    Args:
        waveform: Depending on the setting of g_psweep and the dimension of input waveform(s), the ipnVRI function returns either a waveform or a family of waveforms
        number: Depending on the setting of g_psweep and the dimension of input waveform(s), the ipnVRI function returns a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ipn_v_r_i_curves():
    """Constructs the waveforms associated with an ipn measurement.

    Args:
        vport:
            Voltage across the output port.
            This argument must be a family of spectrum waveforms (1 point per harmonic), with the option of containing a parametric input power sweep (in dBm).
        harmspur:
            Harmonic index of the spurious voltage contained in o_vport.
            When o_iport is specified, also applies to a current waveform contained in o_iport.
        harmref:
            Harmonic index of the reference voltage contained in o_vport.
            When o_iport is specified, also applies to a current waveform contained in o_iport.
        iport:
            Current into the output port.
            This argument must be a family of spectrum waveforms (1 point per harmonic), with the option of containing a parametric input power sweep (in dBm).
            When specified, power is calculated using voltage and current.
        rport:
            Resistance into the output port.
            When specified and o_iport is nil, the output power is calculated using voltage and resistance.
            Default value: 50.
        ordspur:
            Order or slope of the spurious constant-slope power line.
            Default value: 3.
        epoint:
            Value (in dBm) used to indicate the point where the spurious constant-slope power line begins.
            If g_psweep is t, this value is the input power value of the point on the o_spurious waveform, otherwise this value is paired with the o_spurious value to define the point.
            This point should be in the linear region of operation.
            Default value: If g_psweep is t, the X coordinate of the first point of the o_spurious wave; otherwise a number must be specified.
        psweep:
            Boolean indicating that the input power to the circuit was a parametric sweep.
            The power sweep must be in dBm and must be performed at the lowest parametric level.
            Default value: t.
        epref:
            Value (in dBm) used to indicate the point where the reference constant-slope power line begins.
            If g_psweep is t, this value is the input power value of the point on the o_reference waveform, otherwise this value is paired with the o_reference value to define the point.
            This point should be in the linear region of operation.
            Default value: If f_epoint is not nil, f_epoint; else if g_psweep is t, the X coordinate of the first point of the o_reference wave; else a number must be specified.
        ordref:
            Order or slope of the reference constant-slope power line.
            Default value: 1.
        display_labels:
            Specifies whether to display labels on the plot.
            Valid values:


t: Labels are displayed on the plot.
            nil: Labels are not displayed on the plot.
            Default value: t.

    Returns:
        waveform: A family of waveforms that contains the spurious and reference tangent lines, and when g_psweep is t, contains the spurious and reference waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def kf():
    """Returns the stability factor in terms of the supplied parameters.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22

    Returns:
        waveform: Waveform object representing the stability factor
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def ln():
    """Gets the base-e (natural) logarithm of a waveform or number.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object representing the base-e (natural) logarithm of the input waveform if the input argument is a waveform object, or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def log10():
    """Gets the base-10 logarithm of a waveform or a number.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number that is calculated as the base-10 logarithm of the input number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def lsb():
    """Computes the load stability circles.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        frequency:
            Frequency.
            It can be specified as a scalar or a linear range.
            If it is specified as a linear range, the frequency is swept.
            The linear range is specified as a list with three values: the start of the range, the end of the range, and the increment.
            For example, list(100M 1G 100M) specifies a linear range with the following values:

{ 100M, 200M, 300M, 400M, 500M, 600M, 700M, 800M, 900M, 1G }

In that case, a load stability circle is calculated at each one of the 10 frequencies.

    Returns:
        waveform: Waveform object representing the load stability circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def lshift():
    """Shifts the waveform to the left by the delta value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        delta: Value by which the waveform is to be shifted

    Returns:
        waveform:
            Returns a waveform object representing the input waveform shifted to the left.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def mag():
    """Gets the magnitude of a waveform or number.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def nc():
    """Computes the noise circles.

    Args:
        fmin: Waveform object representing the minimum noise factor
        gmin: Waveform object representing the optimum noise reflection
        rn: Waveform object representing the normalized equivalent noise resistance
        level:
            Level in dB.
            It can be specified as a scalar or a vector.
            The level is swept, if it is specified as a vector.
            The linRg function can be called to generate a linear range.
            For example, linRg( -30 30 5 ) is the same as list(-30 -25 -20 -15 -10 -5 0 5 10 15 20 25 30) and the g_level argument can be specified as either of the above.
            In that case, a noise circle is calculated at each one of the 13 levels.
        frequency:
            Frequency.
            It can be specified as a scalar or a linear range.
            The frequency is swept if it is specified as a linear range.
            The linear range is specified as a list with three values: the start of the range, the end of the range, and the increment.
            For example, list(100M 1G 100M) specifies a linear range with the following values:

{100M, 200M, 300M, 400M, 500M, 600M, 700M, 800M, 900M, 1G }

In that case, a noise circle is calculated at each one of the 10 frequencies.

    Returns:
        waveform: Waveform object representing the noise circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def normal_q_q():
    """Returns a quantile-quantile plot of the sample quantiles versus theoretical quantiles from a normal distribution.

    If the distribution is normal, the plot is close to a linear waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns the waveform representing the normal quantile plot
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def overshoot():
    """Computes the percentage by which an expression overshoots a step going from the initial value to the final value you enter.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        init_val: Initial X value at which to start the computation
        init_type:
            Specifies how initVal functions.
            Valid values: a non-nil value specifies that the initial value is taken to be the value of the waveform, interpolated at initVal, and the waveform is clipped from below, as follows:

o_waveform = clip( o_waveform initVal nil )

nil specifies that initVal is defined by the X value entered.
            (The command gets the Y value for the specified X value and uses that value for initVal.
            ).
        final_val: Final value at which to end the computation
        final_type:
            Specifies how finalVal functions.
            Valid values: a non-nil value specifies that the final value is taken to be the value of the waveform, interpolated at finalVal, and the waveform is clipped from above, as follows:

o_waveform = clip( o_waveform nil finalVal )

nil specifies that finalVal is defined by the X value entered.
            (The command gets the Y value for the specified X value and uses that value for finalVal.
            ).
        multiple:
            An optional boolean argument that takes the value nil by default.
            If set to t, the function returns multiple occurrences of the overshoot event.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: 'time, 'cycle.
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the riseTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of riseTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integer

Default value: nil.

    Returns:
        waveform: Returns a waveform (or family of waveforms) representing the amount of overshoot in comparison to the whole signal if the input argument is a family of waveforms or if g_multiple is set to t
        value: Returns a value for the amount of overshoot in comparison to the whole signal if the input is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pavg():
    """Computes the periodic average of a family of signals for each time point.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like srrWave:XXXXX.
            ).
        from: Starting numeric value for the range on the X-axis
        to: Ending numeric value for the range on the X-axis
        period: Numeric value for the period of the input waveform
        sfactor:
            Sampling factor.
            This can be increased in order to increase the accuracy of the output.
            Default value: 1.

    Returns:
        waveform: Returns a waveform representing the periodic average of a family of signals
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def peak():
    """Detects the peaks in the input waveform and returns the X and Y coordinates of these peak points in the form of a waveform.

    Args:
        waveform: Input waveform
        from:
            The initial point on the given waveform to start determining the peaks.
            By default, the first point of the waveform is the starting point.
        to:
            The final point on the given waveform up to which the peaks are to be determined.
            By default, the last point of the waveform is the end point.
        xtol:
            The distance on the X axis within which all peaks are to be filtered.
            Default: 0.
            0.
        ytol:
            The distance on the Y axis within which all peaks are to be filtered.
            Default: 0.
            0.
        with_last:
            Determines whether to include the last point in the peak calculation or not.
            When this argument is set to t, the last point is included in the plot if it is a higher than the previous point.
            When set to nil, the plot stops at the last peak.

    Returns:
        waveform: Returns a waveform whose X and Y coordinates of the peaks are determined from the input waveform and the peaks are filtered based on thef_xtol and f_ytol criteria
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def peak_to_peak():
    """Returns the difference between the maximum and minimum values of a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        overall:

    Returns:
        waveform: Returns a waveform or a family of waveforms if the input argument is a family of waveforms
        value: Returns the difference between the maximum and minimum values of a waveform if the input argument is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def period_jitter():
    """Computes the period jitter.

    It returns a waveform or a value representing deviation from the average period.

    Args:
        waveform: Name of the signal, expression, or a family of waveforms
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            Valid values: rising and falling.
            Default value: rising.
        mode:
            The mode for calculating the threshold.
            Valid values: auto and user.
            If set to user, an n_threshold value needs to be specified by you.
            If set to auto, n_threshold is calculated as:

Auto Threshold Value = integral of the waveform divided by the X range

Default value: auto.
        threshold:
            The threshold value against which the period is to be calculated.
            It needs to be specified only when the mode selected is user.
        bin_size:
            The width of the moving average window.
            The deviation of value at the particular point from the average of this window is the jitter.
            If binsize=0, all periods are used to calculate the average.
            If binsize=N, the last N periods are used to calculate the average.
            Default value: 0.
        x_name:
            The X-axis of the output waveform.
            It specifies whether you want to retrieve the period jitter against time (or another X-axis parameter for non-transient data) or cycle.
            Cycle numbers refer to the n'th occurrence of the delay event in the input waveform.
            Valid values: time and cycle.
            Default value: time.
        output_type:
            Type of output.
            Valid values: sd and plot.
            If set to plot, the output is a jitter waveform.
            If set to sd, the output is a standard deviation of the jitter waveform.
            Default value: plot.

    Returns:
        waveform: Returns the period jitter values as a function of time or cycle when the outputType is set to plot
        val: Returns the standard deviation value when the outputType is set to sd
        nil: Returns nil otherwise
    """
    raise NotImplementedError


def phase():
    """Gets the phase of the waveform or number.

    The phase command is similar to the phaseDegUnwrapped command and returns the unwrapped phase in degrees.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform: Returns a waveform object if the input argument is a waveform object or returns a family of waveforms if the input argument is a family of waveforms
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def phase_deg():
    """Calculates the wrapped phase in degrees of a waveform and returns a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform:
            Returns a waveform object representing the wrapped phase in degrees of the input waveform.
            Returns a family of waveforms if the input argument is a family of waveforms.
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def phase_deg_unwrapped():
    """Calculates the unwrapped phase in degrees of a waveform and returns a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform:
            Returns a waveform object representing the unwrapped phase in degrees of the input waveform.
            Returns a family of waveforms if the input argument is a family of waveforms.
        number: Returns a number if the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def phase_margin():
    """Computes the phase margin of the loop gain of an amplifier.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns a waveform representing the phase margin of the loop gain of an amplifier for a family of waveforms if the input argument is a family of waveforms
        value: Returns the value (in degrees) equivalent to the phase margin of the input waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def phase_rad():
    """Calculates the wrapped (discontinuous) phase in radians of a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number: Number

    Returns:
        waveform:
            Returns a waveform representing a discontinuous value (in radians) for the phase of the input waveform.
            Returns a family of waveforms if the input argument is a family of waveforms.
        number: Returns a number when the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def phase_rad_unwrapped():
    """Calculates the unwrapped (continuous) phase in radians of a waveform and returns a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform:
            Returns a waveform representing the unwrapped (continuous) value for the phase of the input waveform in radians.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def p_n():
    """Calculates the transient phase noise of the input waveforms in decibels (dBc/Hz).

    Phase noise is defined as the power spectral density of the absolute jitter of an input waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        cross_type:
            The points at which the curves of the waveform intersect with the threshold.
            While intersecting, the curve may be either rising or falling.
            Valid values: rising and falling, respectively.
            Default crossType is rising.
        window_name:
            The window type.
            Valid values: 'Blackman, 'Cosine2, 'Cosine4, 'ExtCosBell, 'HalfCycleSine, 'HalfCycleSine3 or 'HalfCycleSine6, 'Hamming, 'Hanning, 'Kaiser, 'Parzen, 'Rectangular, 'Triangular, or 'Nuttall.
            Default value: 'Rectangular.
        smooth:
            The Kaiser window smoothing parameter.
            The 0 value requests no smoothing.
            Valid values: 0 <= x_smooth <= 15.
            Default value: 1.
        windowsize:
            The number of frequency domain points to use in the Fourier analysis.
            A larger window size results in an expectation operation over fewer samples, which leads to larger variations in the power spectral density.
            A small window size can smear out sharp steps in the power spectral density that might really be present.
            Default value: 256.
        detrending:
            The detrending mode to use.
            Valid values: 'None, 'mean, 'Linear

Default value: 'Mean.
        coh_gain:
            A scaling parameter.
            A non-zero value scales the power spectral density by 1/(f_cohGain).
            Valid values: none, default, magnitude, dB20, or dB10

Default value: db20.

    Returns:
        waveform: The power spectral density waveform returned when the command is successful
        nil: Returns nil when the command fails
    """
    raise NotImplementedError


def pow():
    """Takes the exponent of a given waveform or number.

    Args:
        waveform_base: Waveform object to be used as the base for the expression
        waveform_expn: Waveform object to be used as the exponent for the expression
        number_base: Number to be used as the base for the expression
        number_expn: Number to used as the exponent for the expression

    Returns:
        waveform: Returns a family of waveforms if one of the input arguments is a family of waveforms or returns a waveform if one of the input arguments is a waveform (and none is a family)
        result: Returns a number if both the input arguments are numbers
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def prms():
    """Computes the periodic root mean square of a family of signals for each time point, which is the square root of the periodic average of the square of the input waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like srrWave:XXXXX.
            ).
        from: Starting numeric value for the range on the X-axis
        to: Ending numeric value for the range on the X-axis
        period: Numeric value for the period of the input waveform
        sfactor:
            Sampling factor.
            This can be increased in order to increase the accuracy of the output.
            Default value: 1.

    Returns:
        waveform: Returns a waveform representing the periodic root mean square of a family of signals
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def psd():
    """Returns an estimate for the power spectral density of o_waveform.

    If x_windowsize is not a power of 2, it is forced to the next higher power of 2.
    If x_num is less than x_windowsize, x_num is forced to x_windowsize.

    Args:
        waveform: Time domain waveform object with units of volts or amps
        time_start:
            Starting time for the spectral analysis interval.
            Use this parameter and f_timeEnd to exclude part of the interval.
            For example, you might set these values to discard initial transient data.
        time_end: Ending time for the spectral analysis interval
        num:
            The number of time domain points to use.
            The maximum frequency in the Fourier analysis is proportional to x_num and inversely proportional to the difference between f_timeStart and f_timeEnd.
            Default value: 512.
        window_name:
            The window to be used for applying the moving window FFT.
            Valid values: Blackman, Cosine2, Cosine4, ExtCosBell, HalfCycleSine, Half3CycleSine or HalfCycleSine3, Half6CycleSine or HalfCycleSine6,Hamming, Hanning, Kaiser, Parzen, Rectangular, Triangle, Triangular, or Nuttall.
            Default value: Hanning.
        smooth:
            The Kaiser window smoothing parameter.
            The 0 value requests no smoothing.
            Valid values: 0 <= x_smooth <= 15.
            Default value: 1.
        coh_gain:
            A scaling parameter.
            A non-zero value scales the power spectral density by 1/(f_cohGain).
            Valid values: 0 < f_cohGain < 1 (You can use 1 if you do not want the scaling parameter to be used)

Default value: 1.
        window_size:
            The number of frequency domain points to use in the Fourier analysis.
            A larger window size results in an expectation operation over fewer samples, which leads to larger variations in the power spectral density.
            A small window size can smear out sharp steps in the power spectral density that might really be present.
            Default value: 256.
        detrending:
            The detrending mode to use.
            Valid values: mean, linear, none

Default value: none

The psd function works by applying a moving windowed FFT to time-series data.
            If there is a deterministic trend to the underlying data, you might want to remove the trend before performing the spectral analysis.
            For example, consider analyzing phase noise in a VCO model.
            Without the noise, the phase increases more or less linearly with time, so it is appropriate to set the detrending mode to 'linear.
            To subtract an average value, set the detrending mode to 'mean.
            Where the spectrum of raw data is desired, set the detrending mode to none.

    Returns:
        waveform_real: The power spectral density waveform returned when the command is successful
        nil: Returns nil when the command fails
    """
    raise NotImplementedError


def psdbb():
    """Returns an estimate for the power spectral density of o_waveform1+j*o_waveform2.

    If x_windowsize is not a power of 2, it is forced to the next higher power of 2.
    If x_num is less than x_windowsize, x_num is forced to x_windowsize.

    Args:
        waveform1: Time domain waveform object with units of volts or amps
        waveform2: Time domain waveform object with units of volts or amps
        time_start:
            Starting time for the spectral analysis interval.
            Use this parameter and f_timeEnd to exclude part of the interval.
            For example, you might set these values to discard initial transient data.
        time_end: Ending time for the spectral analysis interval
        num:
            The number of time domain points to use.
            The maximum frequency in the Fourier analysis is proportional to x_num and inversely proportional to the difference between f_timeStart and f_timeEnd.
        window_name:
            The window to be used for applying the moving window FFT.
            Valid values: Blackman, Cosine2, Cosine4, ExtCosBell, HalfCycleSine, Half3CycleSine or HalfCycleSine3, Half6CycleSine or HalfCycleSine6, Hamming, Hanning, Kaiser, Parzen, Rectangular, Triangle, Triangular, or Nuttall.
            Default value: Hanning.
        smooth:
            The Kaiser window smoothing parameter.
            0 requests no smoothing.
            Valid values: 0 <= x_smooth <= 15.
            Default value: 1.
        coh_gain:
            A scaling parameter.
            A non-zero value scales the power spectral density by 1/(f_cohGain).
            Valid values: 0 < f_cohGain < 1 (You can use 1 if you do not want the scaling parameter to be used)

Default value: 1.
        window_size:
            The number of frequency domain points to use in the Fourier analysis.
            A larger window size results in an expectation operation over fewer samples, which leads to larger variations in the power spectral density.
            A small window size can smear out sharp steps in the power spectral density that might really be present.
            Default value: 256.
        detrending:
            The detrending mode to use.
            Valid values: mean, linear, none

Default value: none

The psd function works by applying a moving windowed FFT to time-series data.
            If there is a deterministic trend to the underlying data, you might want to remove the trend before performing the spectral analysis.
            For example, consider analyzing phase noise in a VCO model.
            Without the noise, the phase increases more or less linearly with time, so it is appropriate to set the detrending mode to 'linear.
            To subtract an average value, set the detrending mode to 'mean.
            Where the spectrum of raw data is desired, set the detrending mode to 'none.

    Returns:
        waveform_real: The power spectral density waveform returned when the command is successful
        nil: Returns nil when the command fails
    """
    raise NotImplementedError


def pstddev():
    """Computes the periodic standard deviation of a family of signals for each time point.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like srrWave:XXXXX.
            ).
        from: Starting numeric value for the range on the X-axis
        to: Ending numeric value for the range on the X-axis
        period: Numeric value for the period of the input waveform
        sfactor:
            Sampling factor.
            This can be increased in order to increase the accuracy of the output.
            Default value: 1.

    Returns:
        waveform: Returns a waveform representing the periodic standard deviation of a family of signals
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pzbode():
    """Calculates and plots the transfer function of a circuit from pole zero simulation data.

    Args:
        transfer_gain: The transfer gain constant
        minfrequency: The minimum frequency for the bode plot
        maxfrequency: The maximum frequency for the bode plot
        npoints: The frequency interval for the bode plot, in points per decade
        poles:
            Poles from the dumped simulation data.
            Default value: all.
        zeros:
            Zeros from the dumped simulation data.
            Default value: all.

    Returns:
        waveform:
            Waveform containing the X and Y points of the transfer function.
            The scale of the Y-axis will be db20.
        nil: Returns nil and error message otherwise
    """
    raise NotImplementedError


def pzfilter():
    """Returns the filtered Pole and Zero waveforms.

    Args:
        pole_waveform:
            Input Pole waveform (complex points).
            Default value: Poles of the simulator pz-analysis dump.
        zero_waveform:
            Input Zero waveform (complex points).
            Default value: Zeros of the simulator pz-analysis dump.
        maxfreq:
            Maximum frequency.
            Default value: 1e10.
        reldist:
            Relative distance to be considered while filtering.
            Default value: 0.
            05.
        absdist:
            Absolute distance to be considered while filtering.
            Default value: 1e-6.
        minq: Minimum q factor to be allowed while filtering
        output_type:
            Specifies the type of the output.
            If this argument is not passed, the output is a family of waves with two child waveforms, representing poles and zeros respectively, with the real component of each waveform as the X values and the imaginary components as the Y values.
            Valid value: complexwave.
            The output is a family of waves with two child waves, both of which are complex and represent poles and zeros, respectively.

    Returns:
        waveform: Returns a family (waveform) of Pole and Zero waveforms
        nil: Returns nil otherwise
    """
    raise NotImplementedError


def rapid_i_p_n_curves():
    """Plots IPN curves.

    Args:
        result: Object representing simulation results that can be displayed as a series of points on a grid
        results_dir: Name of the directory where results are saved
        resistance: Value of resistance

Default value: 50
        rest:
            List of arguments to be used by the value function on the results data.
            Refer to the value function for more details.

    Returns:
        waveform_real: Returns a waveform
        nil: Returns nil or an error message otherwise
    """
    raise NotImplementedError


def rapid_i_i_p_n():
    """Plots the input IPN curves.

    Args:
        result: Object representing simulation results that can be displayed as a series of points on a grid
        results_dir: Name of the directory where results are saved
        resistance: Value of resistance

Default value: 50
        args:
            List of arguments to be used by the value function on the results data.
            Refer to the value function for more details.

    Returns:
        waveform: Returns a waveform
        nil: Returns nil or an error message otherwise
    """
    raise NotImplementedError


def real():
    """Returns the real part of a waveform representing a complex number, or returns the real part of a complex number.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        input: Complex number

    Returns:
        waveform_real: Returns a waveform when the input argument is a waveform
        number_real: Returns a number when the input argument is a number
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rise_time():
    """Returns the rise time measured between theta1 (percent low) to theta2 (percent high) of the difference between the initial value and the final value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        init_val: Initial value at which to start the computation
        init_type:
            Specifies how n_initVal functions.
            Valid values: a non-nil value specifies that the initial value is taken to be the value of the waveform, interpolated at n_initVal, and the waveform is clipped from below as follows:

o_waveform = clip( o_waveform g_initVal nil ) 

where nil specifies that n_initVal is defined by the X value entered.
            (The command gets the Y value for the specified X value and uses that value for n_initVal.
            ).
        final_val: Final value at which to end the computation
        final_type:
            Specifies how the n_finalVal argument functions.
            Valid values: a non-nil value specifies that the final value is taken to be the value of the waveform, interpolated at n_finalVal, and the waveform is clipped from above, as follows:

o_waveform = clip(o_waveform nil n_finalVal)

where nil specifies that the n_finalVal argument is defined by the X value entered.
            (The command gets the Y value for the specified X value and uses that value for n_finalVal.
            ).
        theta1: Percent low
        theta2: Percent high
        multiple:
            An optional boolean argument that takes the value nil by default.
            If set to t, the function returns multiple occurrences of the riseTime event.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: 'time, 'cycle.
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the riseTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of riseTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integer

Default value: nil.

    Returns:
        waveform: Returns a waveform representing the rise time for a family of waveforms if the input argument is a family of waveforms or if g_multiple is set to t
        value: Returns a value for the rise time if the input is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rms():
    """Returns the root-mean-square value of a waveform.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform: Returns a waveform representing the root-mean-square value for a family of waveforms if the input argument is a family of waveforms
        value: Returns a value for the root-mean-square value for the specified waveform if the input is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rms_noise():
    """Computes the integrated root-mean-square noise over the specified bandwidth.

    Args:
        from: Frequency in hertz that specifies the minimum value for the bandwidth
        to: Frequency in hertz that specifies the maximum value for the bandwidth

    Returns:
        waveform: Returns a waveform (or a family of waveforms) representing the integrated root-mean-square noise if the data being analyzed is parametric
        value: Returns a value for the integrated root-mean-square noise if the data being analyzed is from a single simulation run
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rms_voltage():
    """Calculates the root-mean-square voltage between two nets for fast and regular envelop analysis.

    Args:
        net: Name of the net selected in the schematic
        net1:
            Name of the second net selected in the schematic.
            This argument is optional.
            If not specified, the default value is assumed as gnd.

    Returns:
        voltage: Returns a value in terms of voltage
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rms_terminal_voltage():
    """Calculates the root-mean-square voltage between two terminals for fast and regular envlp analysis.

    Args:
        terminal: Name of the terminal selected in the schematic
        terminal1:
            Name of the second terminal selected in the schematic.
            This argument is optional.
            If not specified, the default value is assumed as gnd.

    Returns:
        voltage: Returns a value in terms of voltage
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def root():
    """Returns the nth X value at which the Y value equals the specified Y value (rootVal).

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        root_val: Y value of interest
        n:
            Number that specifies which X value to return.
            If n equals 1, the first X value that crosses over the Y rootVal is returned.
            If n equals 2, the second X value that crosses over the Y rootVal is returned, and so on.
            If you specify a negative integer for n, the X values that cross the rootVal are counted from right to left (from maximum to minimum).
            If you specify n as 0, the list of root values is returned.

    Returns:
        waveform: Returns a waveform if the input argument is a family of waveforms
        value: Returns an X value when the input argument is a single waveform
        value: Returns a list of all the root values when n is 0
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rshift():
    """Shifts the waveform to the right by the n_delta value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        delta: Value by which the waveform is to be shifted

    Returns:
        waveform:
            Returns a waveform object.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def sample(waveform, start, stop, type, step):
    """Samples a waveform at the specified interval.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: Starting value for the sampling
        to: Ending value for the sampling
        type:
            Type of the sampling.
            Valid values: "linear" or "log".
        by: Interval at which to sample

    Returns:
        waveform: Returns a waveform representing the sampling you specified
        number: Returns a number if the output contains only one point
        nil: Returns nil and an error message otherwise
    """
    return RemoteWaveform(ws['sample'](waveform, start, stop, type, step))


def settling_time():
    """The settling time is the time by which the signal settles within the specified Percent of step (theta) of the difference between the Final Value and Initial Value from the Final Value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        init_val: Initial value at which to start the computation
        init_type:
            Specifies whether the values entered are X values or Y values.
            Valid values: t specifies that initVal is defined by the X value entered; nil specifies that initVal is defined by the Y value entered.
        final_val: Final value at which to start the computation
        final_type:
            Specifies whether the values entered are X values or Y values.
            Valid values: t specifies that finalVal is defined by the X value entered; nil specifies that finalVal is defined by the Y value entered.
        theta:
            Percent of the total step.
            g_multiple

An optional boolean argument that takes the value nil by default.
            If set to t, the function returns multiple occurrences of the settlingTime event.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: 'time, 'cycle.
    """
    raise NotImplementedError


def slew_rate():
    """Computes the average rate at which an expression changes from theta1 (percent low) to theta2 (percent high) of the difference between the initial value and final value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        init_val: Initial X-axis value at which to start the computation
        init_type:
            Specifies whether the values entered are X values or Y values.
            Valid values: t specifies that initVal is defined by the X value entered; nil specifies that initVal is defined by the Y value entered.
        final_val: Final value at which to end the computation
        final_type:
            Specifies whether the values entered are X values or Y values.
            Valid values: t specifies that finalVal is defined by the X value entered; nil specifies that finalVal is defined by the Y value entered.
        theta1: Percent low (percentage of the total step)
        theta2: Percent high (percentage of the total step)
        multiple:
            An optional boolean argument that takes the value nil by default.
            If set to t, the function returns multiple occurrences of the slewRate event.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: 'time, 'cycle.
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the riseTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of riseTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integer

Default value: nil.

    Returns:
        waveform: Returns a waveform representing the slew rate for a family of waveforms if the input argument is a family of waveforms or if g_multiple is set to t
        value: Returns a value for the slew rate for the specified waveform if the input is a single waveform
        nil: Returns nil or an error message otherwise
    """
    raise NotImplementedError


def smith_type():
    """Sets the Smith display mode type for the active graph.

    Args:
        mode:
            Type of Smith display.
            Valid Values:


impedance: Circular graph, also known as Z Smith, where the region above the x-axis repre-sents inductive impedances and the region below the x-axis represents capacitive impedances.
            admittance: Circular graph, also known as Y Smith, where the region above the x-axis repre-sents capacitive admittances and the region below the x-axis represents inductive admittances.
            polar: plot graph, representing data using the polar coordinates system.

    Returns:
        t: Returns t when the specified Smith display id set
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def spectral_power():
    """Returns the spectral power given the spectral current and voltage.

    Args:
        current:
            Waveform representing the current.
            The current can be obtained by calling the i data access function for the desired terminal.

    Returns:
        power: Waveform representing the power of the net
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def spectrum_meas():
    """Calculates Signal-to-Noise-and-Distortion Ratio (SINAD), Spurious Free Dynamic Range (SFDR), Effective Number of Bits (ENOB), and Signal-to-Noise Ratio (without distortion) by using discrete fourier transform of any given input signal.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: The X-axis start value of the portion of input o_waveform to be used for FFT and subsequent calculations
        to: The X-axis end value of the portion of input o_waveform to be used for FFT and subsequent calculations
        num_samples:
            Optional number of sampled points used for the FFT.
            Valid values: Any integer power of two greater than zero.
            Default value: Number of data points in the signal o_waveform.
        noise_bins:
            Optional number of noise bins, where the size of one bin is the reciprocal of the data window width.
            For example, 1 ms of transient data creates a bin size of 1 kHz.
            Valid values: Any integer power of two greater than or equal to zero.
            Default value: 0, implying that no signal is spilling into the bins.
            A frequency band of bin-size times the number of bins is calculated and adjusted as a function of the selected window.
            Frequency components in each band to the left and right of the fundamental or the harmonics are set to zero and do not contribute to any output result.
        start_freq:
            Optional lower limit of frequency range for the spectrum measures.
            Default value: First frequency point of the FFT.
        end_freq:
            Optional upper limit of frequency range for the spectrum measures.
            Default value: Last frequency point of the FFT.
        window_name:
            Optional windowing function applied to o_waveform.
            Valid values: Blackman, Cosine2, Cosine4, ExtCosBell, HalfCycleSine, HalfCycleSine3, HalfCycleSine6, Hamming, Kaiser, Parzen, Rectangular, and Triangular.
            Default value: Rectangular.
        adc_span:
            Optional full-scale span, ignoring any DC offsets.
            This is used in ENOB calculation.
            Valid values: Any floating point number.
            Default value: If n_adcSpan is not specified or is nil, it is assumed to be 0 and is taken to be the peak-to-peak value of the fundamental.
        meas_type:
            Result specifier.
            Valid values: sinad, sfdr(db), enob, and snhr.

    Returns:
        spectrum_waveform: Returns a waveform of spectrum measures
        value: Returns the spectrum measure specified by the t_measType argument
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def spectrum_measurement():
    """Calculates Signal-to-Noise-and-Distortion Ratio (SINAD), Spurious Free Dynamic Range (SFDR), Effective Number of Bits (ENOB), and Signal-to-Noise Ratio (without distortion) by using Fast Fourier Transform (FFT) of any given input signal.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        is_time_wave: Boolean that specifies whether the input wave type is time domain waveform or frequency domain waveform
        from: The X-axis start value of the portion of input o_waveform to be used for FFT and subsequent calculations
        to: The X-axis end value of the portion of input o_waveform to be used for FFT and subsequent calculations
        num_samples:
            Number of sampled points used for the FFT.
            Valid values: Any integer power of two greater than zero.
            For a value that is not a power of two, the function rounds it up to the next closest power of two.
            Default value: Number of data points in the Signal.
        start_freq:
            Lower limit of frequency range for the spectrum measures.
            Default value: First frequency point of the FFT.
        end_freq:
            Upper limit of frequency range for the spectrum measures.
            Default value: Last frequency point of the FFT.
        signal_bins:
            Number of signal bins.
            When you select a window type, this field displays the default number of bins for the selected window type.
            For example, if you select the Window Type as Kaiser that has two signal bins, this field displays 2.
            You can increase the number of signal bins to up to half the value of the sample count.
            For example, if the sample count is 16 for the window type Kaiser, you can increase the signal bin count in the Signal Bins field up to 8.
            You cannot decrease the displayed signal bin value.
            Valid values: 0 to 99.
            Default value: 0.
        window_name:
            Windowing function applied to o_wave while applying the FFT for measurement calculations.
            Valid values: Blackman, Cosine2, Cosine4, ExtCosBell, HalfCycleSine, HalfCycleSine3, HalfCycleSine6, Hanning, Hamming, Kaiser, Parzen, Rectangular, and Triangular.
            Default value: Rectangular.
        sat_lvl:
            Peak saturation level of the FFT waveform.
            Magnitude of the FFT wave is divided by the Peak Sat Level before using it in calculations.
            Peak sat level is the full-scale span ignoring any DC offsets and used in ENOB calculation.
            Valid values: Any floating point number.
            Default value: 0.
        is_noise_analysis: Boolean that specifies whether the analysis type is Signal Analysis or Noise Analysis
        no_of_harmonics:
            Number of harmonics for the waveform that you want to plot.
            For example, If this variable is n, where n should be greater than 1 and the fundamental frequency is harmonic 1, the n harmonics are considered for the harmonic power calculation.
            The signal bins are used for calculating the harmonic power.
            For example, to calculate the total harmonic distortion (THD), if you set the Harmonics value to n, where n is greater than 1, and the fundamental frequency is harmonic 1, the number of harmonics used to calculate THD is 2,.
            ,n.
            If n=3, the 2nd and 3rd harmonics are used to calculate THD.
        meas_type:
            Result specifier.
            Valid values: sinad, sfdr(db), enob, and snhr.
            Default value: sinad.

    Returns:
        value: Returns the spectrum measure specified by the t_measType argument
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ssb():
    """Computes the source stability circles.

    Args:
        s11: Waveform object representing s11
        s12: Waveform object representing s12
        s21: Waveform object representing s21
        s22: Waveform object representing s22
        frequency:
            Frequency.
            It can be specified as a scalar or a linear range.
            The frequency is swept if it is specified as a linear range.
            The linear range is specified as a list with three values: the start of the range, the end of the range, and the increment.
            For example, list(100M 1G 100M) specifies a linear range with the following values:

{ 100M, 200M, 300M, 400M, 500M, 600M, 700M, 800M, 900M, 1G }

In that case, a source stability circle is calculated at each one of the 10 frequencies.

    Returns:
        waveform: Waveform object representing the source stability circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def stddev():
    """Computes the standard deviation of a waveform (or a family of waveforms) over its entire range.

    Standard deviation (stddev) is defined as the square-root of the variance where variance is the integral of the square of the difference of the expression f(x) from average (f(x)), divided by the range of x.

    Args:
        waveform:
            Waveform object or family of waveforms representing simulation results that can be displayed as a series of points.
            (A waveform object identifier looks like this: srrWave:XXXXX).
        ?overall:

    Returns:
        stddev: Returns a number representing the standard deviation value of the input waveform
        waveform_stddev: Returns a waveform representing the average value if the input is a family of waveforms
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def tangent():
    """Returns the tangent to a waveform through the point (n_x, n_y) with the given slope.

    Args:
        waveform: Waveform object representing the wave
        x:
            X coordinate of the point.
            The default value is the X coordinate of the first point on the wave.
        y:
            Y coordinate of the point.
            The default value is the Y coordinate at the given or default X coordinate.
        slope:
            Slope of the line.
            Default value: 1.
            0.
        ckm:

    Returns:
        waveform: Wave object representing the line
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def thd():
    """The thd function computes the percentage of total harmonic content of a signal with respect to the fundamental frequency expressed as a voltage percentage.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        from: Starting time for the DFT sample window
        to: Ending time for the DFT sample window
        num: Number of timepoints
        fund:
            Fundamental Frequency of the signal.
            If it is nil or zero then the non-zero frequency contributing to the largest power in the signal is used as the fundamental frequency.
            Otherwise, the harmonic frequency nearest to its value is used as the fundamental frequency.

    Returns:
        waveform: Returns a waveform representing the absolute value of the total harmonic distortion if the input argument is a family of waveforms
        thd_value: Returns the absolute value of the total harmonic distortion of the input waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def thd_fd():
    """The thd_fd function returns the total harmonic distortion of the input waveform.

    Args:
        name: Name of the node for which total harmonic distorted is to be computed
        result: Name of the result of the specified node

    Returns:
        thd_value: Return a value of total harmonic distortion of the input waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def unity_gain_freq():
    """Computes and reports the frequency at which the gain is unity.

    Args:
        gain_freq_waveform: Gain frequency waveform

    Returns:
        frequency: Returns a scalar value representing the frequency at which the gain of the input waveform is unity
        nil: Returns nil otherwise
    """
    raise NotImplementedError


def value():
    """Returns the Y value of a waveform for a given X value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        scale:
            Specifies the interpolation scale for WREAL signals.
            Valid values: linear, log, nil.
            Note that all scale elements after the second element are ignored.
            X is interpolated in linear mode if scale=nil or the first element of scale is linear.
            X is interpolated in log mode if the first element of scale is log.
            Y is interpolated in linear mode if scale has a single element linear or second element is linear.
            Y is interpolated in log mode if scale has a single element log, or second element is log.
        name:
            The name of the innermost or outermost sweep variable.
            If the sweep variable name is not supplied, the innermost sweep variable is used.
        value:
            Value (X value) at which to provide the Y value.
            If a string has been defined for a value or set of values, the string may be used instead of the value.
        period: The interval or period after which the value needs to be computed
        multiple:
            An optional boolean argument that takes the value nil by default.
            If set to t, the function returns multiple occurrences of the interpolated value.
        x_name:
            An optional argument that is used only when g_multiple is set to t.
            It takes the value time by default.
            It controls the contents of the x vector of the waveform object returned by the function.
            Valid values: time, cycle.
        histo_display:
            When set to t, returns a waveform that represents the statistical distribution of the riseTime data in the form of a histogram.
            The height of the bars (bins) in the histogram represents the frequency of the occurrence of values within the range of riseTime data.
            Valid values: t nil

Default value: nil.
        no_of_histo_bins:
            Denotes the number of bins represented in the histogram representation.
            Valid values: Any positive integer

Default value: 1.
        rest:

    Returns:
        waveform: Returns a waveform or a family of waveforms if the input argument is a family of waveforms or if values are expected at multiple points
        value:
            Returns the Y value if the input argument is a single waveform.
            For parametric sweeps, the value might be a waveform that can be printed with the ocnPrint command.
        nil: Returns nil and an error message if the value cannot be printed
    """
    raise NotImplementedError


def xmax():
    """Computes the value of the independent variable (X) at which the Y value attains its maximum value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number_of_peaks:
            Specifies the nth X value corresponding to the maximum Y value.
            For example, if x_numberOfPeaks is 3, the X value corresponding to the third maximum Y value is returned.
            If you specify a negative integer for x_numberOfPeaks, the X values are counted from right to left (from maximum to minimum).
            If x_numberOfPeaks is 0, xmax returns a list of X locations.

    Returns:
        waveform: Returns a waveform (or a family of waveforms) if the input argument is a family of waveforms
        value: Returns the X value corresponding to the peak specified with x_numberOfPeaks if the input argument is a single waveform
        value: Returns a list of X locations when x_numberOfPeaks is 0 and the input argument is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def xmin():
    """Computes the value of the independent variable (X) at which the Y value attains its minimum value.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        number_of_valleys:
            Specifies the nth X value corresponding to the minimum Y value.
            For example, if x_numberOfValleys is 3, the X value corresponding to the third minimum Y value is returned.
            If you specify a negative integer for x_numberOfValleys, the X-values are counted from right to left (from maximum to minimum).
            If x_numberOfValleys is 0, xmin returns a list of X locations.

    Returns:
        waveform: Returns a waveform (or a family of waveforms) if the input argument is a family of waveforms
        value: Returns the X value corresponding to the valley specified with x_numberOfValleys if the input argument is a single waveform
        value: Returns a list of X locations when x_numberOfValleys is 0 and the input argument is a single waveform
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def xval():
    """Returns a waveform whose X vector and Y vector are equal to the input waveform's X vector.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).

    Returns:
        waveform:
            Returns a waveform if the input argument is a single waveform.
            Returns a family of waveforms if the input argument is a family of waveforms.
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ymax():
    """Computes the maximum value of the waveform's Y vector.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        overall:

    Returns:
        max: Returns a number representing the maximum value of Y if the input argument is a single waveform
        waveform_max: Returns a waveform (or family of waveforms) representing the maximum value of Y if the input argument is a family of waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ymin():
    """Computes the minimum value of a waveform's Y vector.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        overall:

    Returns:
        min: Returns a number representing the minimum value of Y if the input argument is a single waveform
        waveform_min: Returns a waveform (or family of waveforms) representing the minimum value of Y if the input argument is a family of waveforms
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ifreq():
    """Returns the current of the terminal at a specified frequency or at all frequencies in the frequency domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac, qpac, and ac.
            Default value: hb.
        terminal: Terminal name on the schematic or signal name from the Results Browser
        freq:
            Frequency for which you want to plot the results.
            It is an optional field.
            Valid values: Any integer or floating point number.
            Default value: nil

When you specify nil, current on all the frequency points are returned.

    Returns:
        waveform: Returns a waveform representing current at a specified frequency or at all frequency points
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def ih():
    """Returns the current of the terminal at a specified harmonic or at all harmonics in the frequency domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac, and qpac.
            Default value: hb.
        terminal: Terminal name on the schematic or signal name from the Results Browser
        hlist:
            Harmonics for which you want to plot the results.
            It is an optional field.
            For analyses, such as hb, pss, pac, and hbac, you can add either single harmonic value or an available list of harmonic values in this field.
            Valid values: Any integer or a list from the available list of harmonics.
            You can find the available harmonics by using the harmonicList function.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing current at a specified harmonic or at all harmonic points
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def itime():
    """Returns the current of the terminal at a specified time point or at all time points in the time domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, and tran.
            Default value: hb.
        terminal: Terminal name on the schematic or signal name from the Results Browser
        time:
            Time points for which you want to plot the results.
            If you specify a time point in this field, the result of the specified time is returned.
            It is an optional field.
            Valid values: Any integer or floating point number.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing current at a specified time point or at all time points
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pir():
    """Returns the spectral power from current and resistance for a specified harmonic list or for all harmonic points.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac and qpac.
            Default value: hb.
        branch1: First branch name on the schematic or signal name from the Results Browser
        branch2: Second branch name on the schematic or signal name from the Results Browser
        resistance:
            The resistance value.
            Valid values: Any integer or floating point number.
        armonic:
            Harmonics for which you want to plot the results.
            It is an optional field.
            For analyses, such as hb, pss, pac, and hbac, you can add either single harmonic value or an available list of harmonic values in this field.
            Valid values: Any integer or a list from the available list of harmonics.
            You can find the available harmonics by using the harmonicList function.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing spectral power from current and resistance for a specified harmonic list
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pm_noise():
    """Returns the modulated phase noise at a specified frequency or for the entire spectrum.

    Args:
        ana:
            Analysis type or analysis name.
            Valid values: pnoise, and hbnoise.
            Default value: pnoise.
        freq:
            Frequency for which you want to calculate the modulated phase noise.
            Valid values: Any integer or floatng point number

Default value: nil, which means the frequency at all points are calculated.
        modifier:
            Modifier to be used.
            Valid values: dBc, normalized, Power, Magnitude, and dBV

Default value: dBc.
        dsb:
            Specifies whether you want to include the double side band.
            Valid values: t and nil

Default value: t.

    Returns:
        pnoise: Returns the modulated phase noise at the specified frequency point
        waveform: Returns a waveform representing the modulated phase noise at all frequency points
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pn():
    """Returns the phase noise at a specified frequency or at all frequency points.

    Args:
        ana:
            Analysis type or analysis name.
            Valid values: pnoise, hbnoise, and qpnoise.
            Default value: pnoise.
        freq:
            Frequency for which you want to calculate the phase noise.
            Valid values: Any integer or floating point number

Default value: nil, which means the frequency at all points are calculated.

    Returns:
        pn: Returns the phase noise at a specified frequency point
        waveform: Returns a waveform representing the phase noise at all frequency points
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pvi():
    """Returns the spectral power from voltage and current for a specified harmonic list or for all harmonics.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac and qpac.
            Default value: hb.
        pos:
            Positive node or net from the schematic or from the Results Browser.
            This field can also contain an explicit voltage value.
        neg:
            Negative node or net from the schematic or from the Results Browser.
            This field can also contain an explicit voltage value.
        branch1: First branch name on the schematic or signal name from the Results Browser
        branch2: Second branch name on the schematic or signal name from the Results Browser
        hlist:
            Harmonics for which you want to plot the results.
            It is an optional field.
            For analyses, such as hb, pss, pac, and hbac, you can add either single harmonic value or available list of harmonic values in this field.
            Valid values: Any integer or a list from the available list of harmonics.
            You can find the available harmonics by using the harmonicList function.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing the spectral power from voltage and current for a specified harmonic list or for all harmonics
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def pvr():
    """Returns the spectral power at a specified harmonic list or at all harmonics with resistor and voltage on the positive and negative nodes.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac and qpac.
            Default value: hb.
        pos:
            Positive node or net from the schematic or from the Results Browser.
            This field can also contain an explicit voltage value.
        neg:
            Negative node or net from the schematic or from the Results Browser.
            This field can also contain an explicit voltage value.
        resistance:
            The resistance value.
            Valid values: Any integer or floating point number.
        hlist:
            Specify the harmonics for which you want to plot the results.
            It is an optional field.
            For analyses, such as hb, pss, pac, and hbac, you can add either single harmonic value or available list of harmonic values in this field.
            Valid values: Any integer or a list from the available list of harmonics.
            You can find the available harmonics by using the harmonicList function.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing the spectral power on specified harmonic list or on all harmonics with resistor and voltage on the positive and negative nodes
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def spm():
    """Returns the waveform for s-parameters.

    Args:
        ana:
            Analysis type or analysis name.
            Valid values: sp, psp, qpsp, and hbsp

Default value: sp.
        index1:
            Port index for sp simulation.
            By default, this field is set to blank.
            Valid values: Available port index, such as 1, 2.
        index1:
            Port index for sp simulation.
            By default, this field is set to blank.
            Valid values: Available port index, such as 1, 2.
        port1:
            Port instance.
            The port instance can be specified only for the differential s-parameter analysis and not applicable for psp, qpsp and hbsp analyses.
            Valid values: Predefined values “c” and “d” for Spectre simulator.
        port2:
            Port instance.
            The port instance can be specified only for the differential s-parameter analysis and not applicable for psp, qpsp and hbsp analyses.
            Valid values: Predefined values “c” and “d” for Spectre simulator.

    Returns:
        waveform: Returns a waveform representing the s-parameters
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def total_noise():
    """Returns the total noise in a specified frequency limit.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are noise, pnoise, qpnoise, and hbnoise.
            Default value: noise.
        sfreq:
            The start frequency.
            Valid values: Any integer or floating point number.
        efreq:
            The end frequency.
            Valid values: Any integer or floating point number.
        instances:
            List of instances or instance names.
            The noise contributed by the instances specified in this field is ignored while calculating the total noise.
            This is an optional field.

    Returns:
        total_noise: Returns the total noise in a specified frequency limit
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def vfreq():
    """Returns the voltage of a net at a specified frequency or at all frequencies in the frequency domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac, qpac, and ac.
            Default value: hb.
        net: Net name from the schematic or signal name from the Results Browser
        freq:
            Frequency for which you want to plot the results.
            It is an optional field.
            Valid values: Any integer value

Default Value: nil.

    Returns:
        waveform: Returns a waveform representing the voltage of net at a specified frequency
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def vfreqterm():
    """Returns the voltage of a terminal at a specified frequency or at all frequencies in the frequency domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are ac, pss, hb, pac, hbac, qpss, and qpac.
            Default value: hb.
        terminal: Terminal name in schematic from the Results Browser
        req:
            Frequency for which you want to plot the results.
            It is an optional field.
            Valid value: Any integer value

Default value: nil.

    Returns:
        waveform: Returns a waveform representing the voltage at a terminal on the specified frequency
        value: Returns the value of voltage at a terminal on the specified frequency
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def vh():
    """Returns the voltage on a net at a specified harmonic or at all harmonics in the frequency domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, qpss, pac, hbac, and qpac.
            Default value: hb.
        net: Net name on the schematic or signal name from the Results Browser
        hlist:
            Harmonics for which you want to plot the results.
            It is an optional field.
            For analyses, such as hb, pss, pac, and hbac, you can add either single harmonic value or available list of harmonic values in this field.
            Valid values: Any integer or a list from the available list of harmonics.
            You can find the available harmonics by using the harmonicList function.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing the voltage on a net on the specified harmonic
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def vhterm():
    """Returns the voltage on a terminal at the specified harmonic or at all the harmonics in the frequency domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are pss, hb, pac, hbac, qpss, and qpac.
            Default value: hb.
        terminal: Terminal name in schematic from the Results Browser
        armonic:
            Harmonics for which you want to plot the results.
            It is an optional field.
            For analyses, such as hb, pss, pac, and hbac, you can add either single harmonic value or available list of harmonic values in this field.
            Valid values: Any integer or a list from the available list of harmonics.
            You can find the available harmonics by using the harmonic list function.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing the voltage at a terminal on the specified harmonic
        value: Returns the value of voltage at a terminal on the specified harmonic
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def vtime():
    """Returns the voltage of a net at a specified time point or at all time points in the time domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are hb, pss, and tran.
            Default value: hb.
        net: Net name from the schematic or signal name from the Results Browser
        time:
            Time points for which you want to plot the results.
            If you specify a time point in this field, the result of the specified time is returned.
            Otherwise, It is an optional field.
            Valid values: Any integer or floating point number.
            Default value: nil.

    Returns:
        waveform: Returns a waveform representing the voltage of net at a specified time point
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def vtimeterm():
    """Returns the voltage of a terminal at a specified time point or at all time points in the time domain.

    Args:
        ana:
            Analysis type or analysis name.
            The available analyses are tran, pss, and hb.
            Default value: hb.
        terminal: Terminal name in schematic from the Results Browser
        ime:
            Time points for which you want to plot the results.
            If you specify a time point in this field, the result of the specified time point is returned.
            Otherwise, it is an optional field.
            Valid value: Any integer or floating point number

Default value: nil.

    Returns:
        waveform: Returns a waveform representing the voltage at a terminal on the specified time point
        value: Returns the value of voltage at a terminal on the specified time point
        nil: Returns nil or an error message
    """
    raise NotImplementedError


def ypm():
    """Returns the waveform for y-parameters.

    Args:
        ana:
            Analysis type or analysis name.
            Valid values: sp, psp, qpsp, and hbsp

Default value: sp.
        index1:
            Port index for sp simulation.
            By default, this field is set to blank.
            Valid values: Available port index, such as 1, 2.
        index1:
            Port index for sp simulation.
            By default, this field is set to blank.
            Valid values: Available port index, such as 1, 2.

    Returns:
        waveform: Returns a waveform representing the y-parameters
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def zpm():
    """Returns the waveform for z-parameters.

    Args:
        ana:
            Analysis type or analysis name.
            Valid values: sp, psp, qpsp, and hbsp

Default value: sp.
        index1:
            Port index for sp simulation.
            By default, this field is set to blank.
            Valid values: Available port index, such as 1, 2.
        index1:
            Port index for sp simulation.
            By default, this field is set to blank.
            Valid values: Available port index, such as 1, 2.

    Returns:
        waveform: Returns a waveform representing the z-parameters
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def b1f():
    """Returns the alternative stability factor in terms of the specified parameters.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object representing the alternative stability factor
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gac_freq():
    """Returns the available power gain circles where the gain is fixed and frequency is swept.

    Args:
        gain: Gain value in dB
        start_freq: Starting frequency
        stop_freq: Ending frequency
        step: Frequency step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gac_gain():
    """Returns the available power gain circles where the frequency is fixed and gain is swept.

    Args:
        freq: Frequency in Hz
        start_gain: Starting gain value
        stop_gain: End gain value
        step: Gain step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmax():
    """Returns the maximum available gain for a two port.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmin():
    """Returns the optimum noise reflection coefficient for NFmin.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmsg():
    """Returns the maximum stable power gain for a two port.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def g_p():
    """Returns the power gain.

    Operating power gain, GP, is defined as the ratio between the power delivered to the load and the power input to the network.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object representing the power gain
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gpc_freq():
    """Returns the operating power gain circles where the gain is fixed and frequency is swept.

    Args:
        gain: Gain value in dB
        start_freq: Starting frequency
        stop_freq: Ending frequency
        step: Frequency step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gpc_gain():
    """Returns the operating power gain circles where the frequency is fixed and gain is swept.

    Args:
        freq: Frequency value in Hz
        start: Starting gain value
        stop: Ending gain value
        step: Gain step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def g_t():
    """Returns the transducer gain.

    Transducer power gain, GT, is defined as the ratio between the power delivered to the load and the power available from the source.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def gmux():
    """Returns the maximum unilateral power gain for a two port.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def kf():
    """Returns the Stern stability factor.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def load_stability():
    """Computes the load stability circles.

    Args:
        start_freq: Start of the frequency range
        stop_freq: End of the frequency range
        step: Frequency step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object representing the load stability circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def nc_freq():
    """Returns the noise circles with fixed gain and swept frequency.

    Args:
        noise_level: Noise level
        start_freq: Starting frequency
        stop_freq: Ending frequency
        step: Frequency step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def nc_gain():
    """Returns the noise circles with fixed frequency and swept noise level.

    Args:
        freq: Fixed frequency
        start_noise_lvl: Starting noise level
        stop_noise_lvl: Ending noise level
        step: Sweeping noise level step size
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def n_f():
    """Returns the noise figure.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def n_fmin():
    """Returns the minimum noise figure.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def rn():
    """Returns the normalized equivalent noise resistance as a function of frequency.

    Args:
        ata_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def source_stability():
    """Computes the source stability circles.

    Args:
        start_freq: Start of the frequency range
        stop_freq: End of the frequency range
        step: Frequency step size to be used
        results_dir: Results directory path

    Returns:
        waveform: Waveform object representing the source stability circles
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def s11():
    """Returns the response at port 1 due to a signal at port 1.

    Args:
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def s12():
    """Returns the response at port 1 due to a signal at port 2.

    Args:
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def s21():
    """Returns the response at port 2 due to a signal at port 1.

    Args:
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError


def s22():
    """Returns the response at port 2 due to a signal at port 2.

    Args:
        results_dir: Results directory path

    Returns:
        waveform: Waveform object
        nil: Returns nil and an error message otherwise
    """
    raise NotImplementedError
