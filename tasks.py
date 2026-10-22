# task.py file for invoke


try:
    from minchin.releaser import make_release
except ImportError:
    print("[WARN] Run 'vendorize' to bootstrap and gain access to 'make_release'")

try:
    from minchin.releaser import vendorize
except ImportError:
    print("[WARN] Install 'minchin.text' to bootstrap")

try:
    from minchin.tasks import check, format_code, lint, update, upgrade

    # the `test` command defaults to `pytest`, while the package uses `green`.
    # That said, `pytest` does run the suite.
except ImportError:
    print("[WARN] Install 'minchin.tasks' for development management tasks.")
