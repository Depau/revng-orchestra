from ..model.configuration import Configuration
from ..executor import Executor


def install_subcommand(sub_argparser):
    cmd_parser = sub_argparser.add_parser("install", handler=handle_install)
    cmd_parser.add_argument("component")
    cmd_parser.add_argument("--force", action="store_true", help="Force execution of the root action")
    cmd_parser.add_argument("--no-merge", action="store_true", help="Do not merge files into Orchestra root")


def handle_install(args, config: Configuration):
    build = config.get_build(args.component)
    executor = Executor(args)
    executor.run(build.install, force=args.force)
