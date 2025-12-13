def bisect(func, xl, xu, tol, max_iter):

    if func(xl) * func(xu) >= 0:
        print("Error: The root is not bracketed. f(lower) and f(upper) must have opposite signs.")
        return None

    iter_count = 0
    xr = 0.0
    ea = 100.0

    print(f"{'Iter':<10} {'Root Estimate':<20} {'Current Error (%)':<20}")
    print("-" * 50)

    while iter_count < max_iter:
        xrold = xr
        xr = (xl + xu) / 2
        iter_count += 1

        if iter_count > 1:
            if xr != 0:
                ea = abs((xr - xrold) / xr) * 100
            else:
                ea = abs(xu - xl)

        test_val = func(xl) * func(xr)

        if test_val < 0:
            xu = xr
        elif test_val > 0:
            xl = xr
        else:
            ea = 0.0

        print(f"{iter_count:<10} {xr:<20.5f} {ea:<20.5f}")

        if ea < tol or iter_count >= max_iter:
            break

    return xr, iter_count