from traefikswarm import Context

def configure_argparser(parser):
    parser.add_argument('service', metavar='SERVICE', help='Service to modify')
    parser.add_argument('--arg-add', help=f'Argument to add', action='append', default=[])
    parser.add_argument('--arg-rm', help=f'Argument to remove', action='append', default=[])

def execute(ctx: Context):
    args = ctx.args
    name = args.service
    svc = ctx.get_service(name) if ctx.stackname else ctx.get_global_service(name)

    if not svc:
        ctx.abort(f'Service {name} not found')

    for arg in args.arg_rm:
        svc.remove_arg(f'--{arg}')
    for arg in args.arg_add:
        svc.ensure_arg(f'--{arg}')